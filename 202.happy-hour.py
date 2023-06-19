class Solution:
    def isHappy(self, n: int) -> bool:
        ocurred = set()

        while True:
            next = self.getNextNumber(n)
            if next == 1:
                return True
            else:
                if next in ocurred:
                    return False
                ocurred.add(next)
                n = next
            
    def getNextNumber(self, n: int) -> int:
        digits = []
        times = 10
        while n != 0:
            tmp = (n % times)
            digit = tmp // (times//10)
            times *= 10
            n -= tmp
            digits.append(digit)
        # print(digits)
        ans = 0
        for d in digits:
            ans += d*d
        return ans

s = Solution()
print(s.isHappy(2))