class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        left = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                nums[idx] = nums[right]
                left = right
                idx += 1
        return idx
                
                                              
                 