class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prevs, nexts, res = [0]*n, [0]*n, [0]*n
        prevs[0] = 1
        nexts[n-1] = 1
        for i in range(1, n):
            prevs[i] = prevs[i-1]*nums[i-1]
            nexts[n-1-i] = nexts[n-i]*nums[n-i]
        for i in range(0, n):
            res[i] = prevs[i]*nexts[i]
        return res 
    # Todo: Try to solve this in O(1) Space complexity