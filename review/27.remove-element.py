from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] != val:
                left += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
        print(nums)
        return left
s = Solution()
print(s.removeElement([2], 2))
print(s.removeElement([2, 3, 3, 2, 3, 2, 3, 1, 4], 2))
