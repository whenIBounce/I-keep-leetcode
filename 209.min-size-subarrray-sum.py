from typing import List
class Solution:
    # TODO: 在复习一遍
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums or sum(nums) < target:
            return 0
        
        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= target:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1
        
        return 0 if ans == n + 1 else ans
    
s = Solution()
print(s.minSubArrayLen(213, [12,28,83,4,25,26,25,2,25,25,25,12]
))