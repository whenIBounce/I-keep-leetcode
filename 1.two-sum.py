from typing import List
class Solution:
    # Method 1: Brute Force
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    # Method 2: Hashmap
    #!!! In method 1, it is the process that looking for
    #!!! target - nums[i] takes most of the time.
    #!!!! By using hashtable, we can save that time
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(0, len(nums)):
            if target - nums[i] in m:
                return [i, m[target-nums[i]]]
            m[nums[i]] = i
        
s = Solution()
print(s.twoSum([3,2,4], 6))