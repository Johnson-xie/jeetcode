class Solution:
    def minCostConnectPoints(self, points) -> int:

        def get_manhadun(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        l = len(points)
        if l <= 1:
            return [], 0

        con = [points[0]]  # 已经连线的点集，先随便放一个点进去
        not_con = points[1:]  # 还没连线的点集
        # paths = []  # 所有连线
        length_total = 0  # 总连线长度
        for _ in range(l - 1):  # 共 l-1 条连线
            # 得到下一条连线的两点a、b 及其距离length_ab
            a, b = con[0], not_con[0]  # 先任意选两个点
            length_ab = get_manhadun(a, b)
            for m in con:
                for n in not_con:
                    lg = get_manhadun(m, n)
                    if lg < length_ab:  # 如果有更短的
                        length_ab = lg
                        a, b = m, n

            # 记录
            # paths.append([points.index(a), points.index(b)])  # 记录连线ab
            con.append(b)  # 已连接点集中记录点b
            not_con.remove(b)  # 未连接点集中删除点b
            length_total += length_ab  # 记录总长度

        return length_total


class Solution2:
    def minCostConnectPoints(self, points) -> int:

        def get_manhadun(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        def juli_point_list(point, list1):
            '''计算点和列表1中所有点最近距离 index向量'''
            juli_list = []
            for i in list1:
                juli_list.append(get_manhadun(point, i))
            start = juli_list.index(min(juli_list))  # 最小距离的索引
            end = len(list1)
            return [start, end]

        res = []
        for i in range(1, len(points)):
            mindistance = juli_point_list(points[i], points[:i])
            res.append(mindistance)
        return res


if __name__ == '__main__':
    # https://blog.csdn.net/lnotime/article/details/82313355#?utm_medium=distribute.pc_relevant_download.none-task-blog-baidujs-2.nonecase&depth_1-utm_source=distribute.pc_relevant_download.none-task-blog-baidujs-2.nonecase
    # points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    points = [[3, 12], [-2, 5], [-4, 1]]
    # points = [[0, 0]]
    ret = Solution2().minCostConnectPoints(points)
    print(ret)
