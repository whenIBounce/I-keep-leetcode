class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) < 1:
            return True
        sptr = 0
        for i in range(0, len(t)):
            if sptr < len(s) and s[sptr] == t[i]:
                sptr += 1
        return sptr == len(s)
                
s = Solution()
print(s.isSubsequence("b", "abc"))
print(s.isSubsequence("bc", "abc"))
print(s.isSubsequence("c", "abc"))
print(s.isSubsequence("ascc", "s"))