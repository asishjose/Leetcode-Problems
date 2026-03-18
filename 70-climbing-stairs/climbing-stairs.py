class Solution:
    def climbStairs(self, n: int) -> int:
        la, s_la = 1, 1
        for i in range(n-1):
            la, s_la = la + s_la, la
        return la