from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cmap = defaultdict(int)
        for c in s:
            cmap[c] += 1
        for c in t:
            cmap[c] -= 1
            if cmap[c] < 0:
                return False
        return True
    
            