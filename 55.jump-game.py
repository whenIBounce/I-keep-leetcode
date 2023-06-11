from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_jump = 0
        
        for i in range(0, n):
            if i <= max_jump:
                max_jump = max(max_jump, i+nums[i])
                if max_jump >= n-1:
                    return True
                i = max_jump

        return False

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
    print("Output:", solution.canJump(nums))
    print()
