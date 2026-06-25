class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        return self.checkNumbers(100, digits, res)

    def checkNumbers(self, n, digits, res):
        if n > 998:
            return res

        if self.numCheck(n, digits):
            res.append(n)

        return self.checkNumbers(n + 2, digits, res)

    def numCheck(self, n, digits):
        digitss = digits.copy()

        for d in map(int, str(n)):
            if d in digitss:
                digitss.remove(d)
            else:
                return False

        return True