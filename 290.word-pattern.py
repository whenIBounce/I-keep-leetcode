class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wmap = {}
        matched = set()
        words = s.split()
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in wmap:
                if words[i] not in matched:
                    wmap[pattern[i]] = words[i]
                    matched.add(words[i])
                else:
                    return False
            else:
                if wmap[pattern[i]] != words[i]:
                    return False
        return True
