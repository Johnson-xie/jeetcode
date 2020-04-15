class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        self.ret = [[]]

        nums.sort()

        def dfs(nums, cur_lst):
            # back point
            if not nums:
                return

            # process
            for index, num in enumerate(nums):
                if index > 0 and num == nums[index - 1]:
                    continue
                if cur_lst and num < cur_lst[-1]:
                    continue
                new_lst = cur_lst + [num]
                self.ret.append(new_lst)
                # drill down
                dfs(nums[:index] + nums[index + 1:], new_lst)

            # clear
            return self.ret

        return dfs(nums, [])

