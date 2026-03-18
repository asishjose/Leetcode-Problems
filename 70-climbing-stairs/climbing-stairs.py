class Solution:
    def climbStairs(self, n: int) -> int:
        la = 1
        s_la = 1
        for i in range(1,n):
            la, s_la = la + s_la, la
        return la