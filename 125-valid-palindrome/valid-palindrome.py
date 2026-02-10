class Solution:
    def isPalindrome(self, s: str) -> bool:
        stri = ""
        for l in s:
            if l.isalnum():
                stri += l.lower()
        
        n = len(stri)
        i = 0
        j = n-1
        while i<j:
            if stri[i]!=stri[j]:
                return False
            i += 1
            j -= 1
        return True