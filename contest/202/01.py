class Solution:
    def minDays(self, n: object) -> object:
        self.min_cnt = float('inf')

        self.cache = set()

        self.backtrace(n, 0)

        return self.min_cnt

    def backtrace(self, n, cnt):
        if n == 0:
            if cnt < self.min_cnt:
                self.min_cnt = cnt
            return
        if cnt >= self.min_cnt:
            return
        if (n, cnt) in self.cache:
            return
        self.cache.add((n, cnt))
        cnt += 1



        if n % 2 == 0:
            self.backtrace(n / 2, cnt)

        if n % 3 == 0:
            self.backtrace(n - 2 * (n / 3), cnt)

        self.backtrace(n - 1, cnt)


if __name__ == '__main__':
    ret = Solution().minDays(7000)
    print(ret)
