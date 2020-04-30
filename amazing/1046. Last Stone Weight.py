import bisect


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            s1, s2 = stones.pop(), stones.pop()
            s3 = abs(s1 - s2)
            if s3 != 0:
                bisect.insort(stones, s3)

        return stones[0] if stones else 0