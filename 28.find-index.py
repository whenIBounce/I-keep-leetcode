class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) <= len(needle):
            if haystack == needle:
                return 0
            else:
                return -1
        for i in range(0, len(haystack)-len(needle)+1):
            complete = True
            tmp = i
            for c in needle:
                if c == haystack[tmp]:
                    tmp += 1
                else:
                    complete = False
                    break
            if complete:
                return i 
        return -1

h = "abc"
n = "c"
s = Solution()
print(s.strStr(h, n))