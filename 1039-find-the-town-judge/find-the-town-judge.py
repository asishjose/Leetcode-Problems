class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting, trusted = set(),[]
        
        for i in range(len(trust)):
            trusting.add(trust[i][0])
            trusted.append(trust[i][1])
        for i in range(1,n+1):
            if i not in trusting:
                if trusted.count(i) == n-1:
                    return i
        return -1