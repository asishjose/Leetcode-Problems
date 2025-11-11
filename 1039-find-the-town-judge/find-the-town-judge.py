class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting, trusted = [],[]
        if not trust and n==1:
            return 1
        for i in range(len(trust)):
            trusting.append(trust[i][0])
            trusted.append(trust[i][1])
        for i in range(n+1):
            if i not in trusting:
                if trusted.count(i) == n-1:
                    return i
        return -1