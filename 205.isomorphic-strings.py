class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cmap = {}
        to = set()

        for i in range(len(s)):
            if s[i] not in cmap:
                if t[i] not in to:
                    cmap[s[i]] = t[i]
                    to.add(t[i])
                else:
                    return False
            else:
                if cmap[s[i]] != t[i]:
                    return False
            
        return True