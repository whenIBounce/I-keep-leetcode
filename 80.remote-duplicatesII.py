class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return
        idx = 2
        for right in range(2, len(nums)):
            if nums[idx-2] != nums[right]:
                nums[idx] = nums[right]
                idx += 1
        return idx