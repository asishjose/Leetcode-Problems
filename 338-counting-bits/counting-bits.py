class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            bit_count = 0
            while i:
                bit_count += i%2
                i = i>>1
            ans.append(bit_count)
        return ans
