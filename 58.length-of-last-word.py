class Solution:
    # METHOD1: 我的第一种解法，低效，这题实际上应该反向遍历
    def lengthOfLastWord2(self, s: str) -> int:
        lw = ""
        prev = ' '
        for c in s:
            if prev == ' ' and c != ' ':
                lw = c + ""
            elif prev != ' ' and c != ' ':
                lw += c
            print(lw)
            prev = c
        return len(lw)
    
    def lengthOfLastWord(self, s: str) -> int:
        lw = ""
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ' and lw != "":
                break
            if s[i] != ' ':
                lw += s[i]
        return len(lw)
s = Solution()
ans = s.lengthOfLastWord(" b")
print(ans)
