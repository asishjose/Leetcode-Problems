class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split()
        words2 = s2.split()
        words = words1+words2
        uncommon = []
        for word in words:
            if words.count(word)==1:
                uncommon.append(word)
        return uncommon