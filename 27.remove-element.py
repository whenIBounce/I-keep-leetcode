from typing import List

class Solution:
    def removeElement2(self, nums: List[int], val: int) -> int:
        swap_index = -1
        count = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val and swap_index == -1:
                count += 1
                continue
            elif nums[i] != val and swap_index == -1:
                swap_index = i
            elif nums[i] == val and swap_index != -1:
                count += 1
                # swap val with nums[swap_index]
                tmp = nums[swap_index]
                nums[swap_index] = val
                nums[i] = tmp
                # find next swap_index
                while swap_index > i and nums[swap_index] == val:
                    swap_index -= 1
            else:
                continue
        return count
    
    def removeElement3(self, nums: List[int], val: int) -> int:
        idx = 0
        for x in nums:
            if x != val:
                nums[idx] = x
                idx += 1
        return idx
    
    def removeElement4(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range(0,len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left
    
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) 
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right-1]
                right -= 1
            else:
                left += 1
        return left
    
# Initialize the class
solution = Solution()

# Create a list and a value to remove
nums = [2,0,1,2,0,2]
val = 2

# Call the method and print the result
result = solution.removeElement(nums, val)
print(result)
