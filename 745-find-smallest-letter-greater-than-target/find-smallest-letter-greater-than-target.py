class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.append(target)
        letters = set(letters)
        letters = list(letters)
        letters.sort()
        if letters[len(letters)-1] == target:
            return letters[0]
        for i in range(len(letters)): 
            if letters[i] == target:
                return letters[i+1]
