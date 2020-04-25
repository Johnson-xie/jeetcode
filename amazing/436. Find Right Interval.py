import bisect


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        interval_table = {}

        for index, value in enumerate(intervals):
            interval_table[tuple(value)] = index

        ret = []

        intervalsed = sorted(intervals)

        for _, (start, end) in enumerate(intervals):
            index = bisect.bisect_right(intervalsed, [start, end])
            for i in range(index, len(intervalsed)):
                start2, end2 = intervalsed[i]
                if start2 >= end:
                    ret.append(interval_table[(start2, end2)])
                    break
            else:
                ret.append(-1)

        return ret

    def findRightInterval2(self, intervals: List[List[int]]) -> List[int]:

        intervalsed = sorted((start, index) for index, (start, _) in enumerate(intervals))

        ret = []

        N = len(intervals)

        for _, end in intervals:
            index = bisect.bisect_right(intervalsed, (end,))
            ret.append(intervalsed[index][1] if index < N else -1)

        return ret

"""待提速"""

