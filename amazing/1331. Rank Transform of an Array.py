class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}

        for num in sorted(arr):
            if num not in rank:
                rank.setdefault(num, len(rank) + 1)

        return map(rank.get, arr)