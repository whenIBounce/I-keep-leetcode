class Solution:
    # Method 1: 直接算每个char的位置
    def convert2(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = ["" for _ in range(numRows)]
        for i in range(0, len(s)):
            r = i%(numRows+numRows-2)
            if r < numRows:
                rows[r] = rows[r] + s[i]
            else:
                r = (numRows+numRows-2) - i%(numRows+numRows-2)
                rows[r] = rows[r] + s[i]
        return "".join(rows)
    # Method: use flag
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        i = 0
        flag = -1
        rows = ["" for _ in range(numRows)]
        for c in s:
            rows[i] = rows[i] + c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag   
        return "".join(rows)
    
s = Solution()
ans = s.convert("PAYPALISHIRING", 3)
print(ans)