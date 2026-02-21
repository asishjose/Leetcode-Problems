class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        b = bin(n)[2:]
        for bit in b:
            if bit == "1":
                res+=1
        return res