class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=lambda x : x != 0)
        print(nums)

        point = 0
        for index, value in enumerate(nums):
            if value != 0:
                point = index
                break

        nums[point:] = list(reversed(nums[point:]))
        print(nums)
        nums.reverse()
        print(nums)

    def moveZeroes2(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p2 = 0, 0
        N = len(nums)

        while p2 < N:
            while p1 < N and nums[p1] != 0:
                p1 += 1

            if p2 <= p1:
                p2 = p1 + 1

            if p2 >= N:
                break

            if nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 += 1
            else:
                p2 += 1



if __name__ == '__main__':
    # nums = [0, 1, 0, 3, 12]
    nums = [1]
    sol = Solution()
    sol.moveZeroes2(nums)
