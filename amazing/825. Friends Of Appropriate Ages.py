class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:

        def request(a, b):
            return not ((b <= 0.5 * a + 7) or (b > a) or (b > 100 and a < 100))

        c = collections.Counter(ages)

        sum_request = 0

        for age_a, cnt1 in c.items():
            for age_b, cnt2 in c.items():
                if age_a == age_b:
                    sum_request += request(age_a, age_b) * cnt1 * (cnt1 - 1)
                else:
                    sum_request += request(age_a, age_b) * cnt1 * cnt2

        return sum_request
