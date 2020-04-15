class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        if not candidates:
            return []

        self.res = []

        candidates.sort()

        def helper(target, lst):
            # back
            if target == 0:
                self.res.append(lst)
                return

            if target < 0:
                return
            # process

            # 优化，新一轮的迭代从元素的索引位置开始循环
            for value in candidates:
                if lst and value < lst[-1]:  # 去重
                    continue
                # drill down
                helper(target - value, lst + [value])

            # clear
            return self.res

        return helper(target, [])

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        if not candidates:
            return []

        self.res = []

        candidates.sort()

        def helper(target, index, lst):
            # back
            if target == 0:
                self.res.append(lst)
                return

            if target < 0:
                return
            # process

            # 优化，新一轮的迭代从元素的索引位置开始循环
            for i in range(index, len(candidates)):
                if lst and candidates[i] < lst[-1]:  # 去重
                    continue
                # drill down
                helper(target - candidates[i], i, lst + [candidates[i]])

            # clear
            return self.res

        return helper(target, 0, [])