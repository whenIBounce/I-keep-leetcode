class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #first missing positive will not be greater than len(nums)
        checks = []
        for i in range(len(nums)+1):
            checks.append(False)
        for num in nums:
            if num >=0 and num <= len(nums):
                checks[num] = True
        for i, check in enumerate(checks):
            if i>0 and not check:
                return i
        return len(nums)+1
            