class Solution:
    def reverseWords2(self, s: str) -> str:
        ans = ""
        prev = ' '
        start = end = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ' and prev == ' ':
                end = i
            if s[i] == ' ' and prev != ' ':
                start = i+1
                ans = ans + s[start:end+1] + ' '
            if i == 0 and s[i] != ' ':
                start = i
                ans = ans + s[start:end+1]
            prev = s[i]
        if ans[-1] == ' ':
            ans =  ans[0:-1]
        return ans
    # TODO: 或者做一个冷酷无情的API选手
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
s = Solution()
a = s.reverseWords("th w")
print(a)