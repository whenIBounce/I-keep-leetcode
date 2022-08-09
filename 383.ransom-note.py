class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        
        for m in magazine:
            letters[m] = letters.get(m, 0) + 1
            
        for r in ransomNote:
            if r not in letters or letters[r] - 1 < 0:
                return False
            else:
                letters[r] = letters[r] - 1

        return True
            
        