class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]

        for num in nums:
            ret.extend([sub + [num] for sub in ret])

        return ret

"""
每遍历一个新的数字，
给已存在的每个子集加一个数字，产生新的一批子集，
全部再添加到集合中

"""