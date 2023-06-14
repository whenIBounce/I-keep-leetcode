from typing import List
class Solution:
    # For Trapping rain water,
    # the most important thing is to realize that
    # the amount of water trapped above a bar 
    # is determined by the height of the tallest bar on its left and right. 
    
    # Method 1:
    def trap2(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0 for _ in range(n)]
        right_max = [0 for _ in range(n)]
        left_max[0] = height[0]
        right_max[-1] = height[-1]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
            right_max[n-i-1] = max(right_max[n-i], height[n-i-1])
        ans = 0
        for i in range(0, n):
            if height[i] < min(left_max[i], right_max[i]):
                ans += min(left_max[i], right_max[i])-height[i]
        return ans
    # Method 2: 2-pointers
    # ? Why does this solution work? 
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 1
        right = n - 2
        left_max = 0
        right_max = 0
        ans = 0
        for i in range(1, n-1):
            if height[left-1] < height[right+1]:
                left_max = max(left_max, height[left-1])
                if height[left] < left_max:
                    ans = ans + (left_max - height[left])
                left += 1
            else:
                right_max = max(right_max, height[right+1])
                if height[right] < right_max:
                    ans = ans + (right_max - height[right])
                right -= 1
        return ans
                
s = Solution()
ans = s.trap([3, 2, 1, 0, 1])
print(ans)