class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ret = []

        if not candidates:
            return []

        candidates.sort()

        def dfs(target, candidates, lst):

            # back
            if target == 0:
                self.ret.append(lst)
                return

            if target < 0 or not candidates:
                return

            # process

            for index, value in enumerate(candidates):
                if value > target or (lst and value < lst[-1]):
                    continue

                # 每一层下去，同样的数只减一次，去重复
                if index > 0 and candidates[index - 1] == candidates[index]:
                    continue
                dfs(target - value, candidates[:index] + candidates[index + 1:], lst + [candidates[index]])

            return self.ret

        return dfs(target, candidates, [])

if __name__ == '__main__':
    sol = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    ret = sol.combinationSum2(candidates, target)
    print(ret)
