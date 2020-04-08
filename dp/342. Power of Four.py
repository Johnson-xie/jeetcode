import math


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and math.log(num, 2) % 2 == 0

    def isPowerOfFour2(self, num: int) -> bool:
        return num != 0 and num &(num-1) == 0 and num & 1431655765== num


"""
1
100
10000
1000000
100000000
10000000000
1000000000000
100000000000000
10000000000000000
1000000000000000000
100000000000000000000
10000000000000000000000
1000000000000000000000000
100000000000000000000000000
10000000000000000000000000000
1000000000000000000000000000000
Any other number not it the list should be considered as invalid.
So if you XOR them altogether, you will get a mask value, which is:


后面这个大数迁就上面所有4的倍数的数
1010101010101010101010101010101 (1431655765)

"""
