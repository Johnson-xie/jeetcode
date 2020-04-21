class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        table = {}

        stack = []

        N = len(nums)

        for index, num in enumerate(nums * 2):
            while stack and stack[-1][0] < num:
                sub_num, sub_index = stack.pop()
                table[(sub_num, sub_index % N)] = num
            stack.append((num, index % N))

        return [table.get((num, index), -1) for index, num in enumerate(nums)]
