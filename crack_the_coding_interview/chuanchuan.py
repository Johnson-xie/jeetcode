"""回溯加缓存"""
import random


class Solution(object):

    def chuanchuan(self, m, employers):
        """
        :param m: 最低串串数
        :param n: 员工效率值列表
        """
        self.cached = set()

        employers = sorted(employers, reverse=True)
        self.diff = float('inf')
        self.ret = []

        self.backtrace(m, [], employers)

        print(self.diff + m)
        print(self.ret)
        return self.ret

    def backtrace(self, left, sum_list, employers):
        if tuple(sorted(sum_list)) in self.cached:
            return
        self.cached.add(tuple(sorted(sum_list)))
        if left <= 0:
            if abs(left) < self.diff:
                self.ret = [sum_list]
                self.diff = abs(left)
            elif abs(left) == self.diff:
                self.ret.append(sum_list)
                self.diff = abs(left)
            return

        if not employers:
            return

        for i in range(len(employers)):
            self.backtrace(left - employers[i], sum_list + [employers[i]], employers[:i] + employers[i + 1:])


if __name__ == '__main__':
    m = random.randint(200, 500)
    n = [random.randint(50, 100) for i in range(30)]
    # m = 1000
    # n = [500, 500, 300, 200]
    print(m)
    print(n)
    Solution().chuanchuan(m, n)
