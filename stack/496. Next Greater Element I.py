"""
2
84
907
1019
768
402
"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}

        stack = []

        for num in nums2:
            if not stack:
                stack.append(num)
            else:
                while stack and num > stack[-1]:
                    table[stack.pop()] = num
                stack.append(num)
        for num in stack:
            table[num] = -1

        return [table[num] for num in nums1]

    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}

        stack = []

        for num in nums2:
            if not stack:
                stack.append(num)
            else:
                while stack and num > stack[-1]:
                    table[stack.pop()] = num
                stack.append(num)

        return [table.get(num, -1) for num in nums1]
