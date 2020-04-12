class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0x100000000
        max_int = 0x7fffffff
        min_int = 0x80000000

        while b:
            # no_advance_sum = a ^ b   # 无进位求和
            # advance_sum = (a & b) << 1
            # a = no_advance_sum
            # b = advance_sum

            a, b = (a ^ b) % mask, ((a & b) << 1) % mask
        return a if a <= max_int else ~((a % min_int) ^ max_int)

"""
         if result & 0x80000000: # 1 in bit number 32
				 result = (result & 0x7fffffff) - 2**31
            #   result = result - 2**32 # Same thing as above
"""