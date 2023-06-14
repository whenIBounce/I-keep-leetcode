class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        romans = {1000:"M", 900:"CM", 500:"D", 
                  400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL",
                  10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        for r in romans:
            while num >= r:
                ans += romans[r]
                num -= r 
        return ans
s = Solution()
s.intToRoman(3999)