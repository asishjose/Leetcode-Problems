class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        if len(s)+len(t) == 0:
            return True
        for i in range(len(t)):
            if j < len(s):
                if s[j] == t[i]:
                    print(s[j], t[i])
                    j+=1
                    if j == len(s):
                        return True
            else:
                return True
        return False