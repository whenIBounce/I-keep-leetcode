from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        ans = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                elif nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                else:
                    ans.append([nums[l], nums[i], nums[r]])
                    while l+1 < len(nums) and nums[l+1] == nums[l]:
                        l += 1
                    while r-1 >= 0 and nums[r-1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
        return ans

s = Solution()
print(s.threeSum([-2,0,0,2,2]))