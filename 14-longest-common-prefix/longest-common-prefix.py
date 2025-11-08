class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
         pref = strs[0]
         pref_len = len(strs[0])

         for s in strs[1:]:
            while pref != s[:pref_len]:
                pref_len -= 1
                pref = pref[:pref_len]
         return pref