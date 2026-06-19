class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"

        def gen_str(w):
            nxt_word = ""
            for c in w:
                nxt_word = nxt_word + chr(ord(c)+1)
            return nxt_word

        def addon(k, word):
            if len(word) >= k:
                return word[k-1]
            word = word + gen_str(word)
            return addon(k, word)
        
        return addon(k, word)