class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        hash = {}
        for c in word:
            if c.lower() not in hash:
                if c.lower() in word and c.upper() in word:
                    hash[c.lower()] = 1
                else:
                    hash[c.lower()] = 0
        print(hash)
        count = sum(1 for val in hash.values() if val == 1)
        return count