import collections
import math


class Solution:
    def getMinDistSum(self, positions) -> float:
        distance = float('inf')
        xrange = min(x for x, _ in positions)
        yrange = min(y for _, y in positions)

        def get_distance(p1, p2):
            return math.sqrt((p1[0] - p2[0]) ** 2+(p1[1] - p2[1]) ** 2)

        return min(sum(get_distance([x, y], p) for p in positions) for x in range(xrange + 1) for y in range(yrange + 1))


class Solution2:
    # table = [0] * 100001
    # table[1] = 1
    # for i in range(2, 100002):
    #     table[i] = table[i - 1] + i
    # print(table)

    def numSub(self, s: str) -> int:
        cnt = 0
        s_list = s.split("0")
        for s in s_list:
            cnt += self.table[len(s)]
        return cnt % (10 ** 9 + 7)


class Solution3:
    def maxProbability(self, n: int, edges, succProb, start: int, end: int) -> float:

        self.ans = 0
        self.table = collections.defaultdict(set)

        for s, e in edges:
            self.table[s].add(e)
            self.table[e].add(s)

        self.p_map = {tuple(key): value for key, value in zip(edges, succProb)}

        self.backtrace(start, end, set(), 1)
        return self.ans

    def backtrace(self, start, end, traverse, probability):
        if start == end:
            self.ans = max(self.ans, probability)
            return

        if probability == 0:
            return

        for next_start in self.table.get(start):
            if next_start not in traverse:
                self.backtrace(next_start, end, traverse | set([next_start]),
                               probability * self.p_map.get((start, next_start), 0))

if __name__ == '__main__':
    # ps = [[0, 1], [1, 0], [1, 2], [2, 1]]
    # res = Solution().getMinDistSum(ps)
    # res = Solution2().numSub('0110111')
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.3]
    start = 0
    end = 2
    res = Solution3().maxProbability(n, edges, succProb, 0, 2)

    print(res)

