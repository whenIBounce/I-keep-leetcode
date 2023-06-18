from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        word = defaultdict(int)
        for m in magazine:
            word[m] += 1
        for r in ransomNote:
            if r not in word:
                return False
            word[r] -= 1
            if word[r] < 0:
                return False
        return True