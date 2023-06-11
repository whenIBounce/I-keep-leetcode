from typing import List
import sys
class Solution:
    # Method 1: dynamic programming
    def jump2(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [sys.maxsize for _ in range(n)]
        dp[0] = 0
        for i in range(0, n):
            steps = nums[i]
            jump_to = min(n-1, i+steps)
            for j in range(i+1, jump_to+1):
                dp[j] = min(dp[j], dp[i]+1)
        return dp[n-1]
    #!!! This method only works when you know that you can reach nums[n-1]
    def jump(self, nums: List[int]) -> int:
        max_jump = 0
        n = len(nums)
        end = 0
        steps = 0
        for i in range(0, n-1): #!!! 注意理解为什么止于n-1
            max_jump = max(max_jump, i+nums[i])
            if end == i:
                steps += 1
                end = max_jump
                
        return steps
                
                
            

test_cases = [
    [2,3,1,1,4],  # Expected output: True
    [3,2,1,0,4],  # Expected output: False
    [0],  # Expected output: True
    [2,5,0,0],  # Expected output: True
    # add more test cases as needed
]

solution = Solution()

for i, nums in enumerate(test_cases):
    print(f"Test case {i+1}:")
    print("Input:", nums)
    print("Output:", solution.jump(nums))
    print()
