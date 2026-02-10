class Solution:
    def isPalindrome(self, s: str) -> bool:
        stri = ""
        for l in s:
            if l.isalpha() or l.isdigit():
                stri += l.lower()
                print(l)

        return stri == stri[::-1]