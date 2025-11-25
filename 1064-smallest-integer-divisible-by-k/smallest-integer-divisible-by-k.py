import sys
sys.set_int_max_str_digits(10000000)  

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:

        if k % 2 == 0 or k % 5 == 0:
            return -1
        length = 1
        remainder = 1
        while remainder % k != 0:
            remainder = (remainder * 10 + 1)%k
            length += 1
        return length