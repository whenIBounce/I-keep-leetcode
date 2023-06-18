class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        left = 0
        contains = set()
        contains.add(s[left])
        ans = 0
        
        for i in range(1, len(s)):
            if s[i] in contains:
                while s[left] != s[i]:
                    contains.remove(s[left])
                    left += 1
                contains.remove(s[left])
                left += 1
                
            contains.add(s[i])
            ans = max(ans, i-left+1)        
        
        return ans


s = Solution()
mys = " "
print(s.lengthOfLongestSubstring(mys))
