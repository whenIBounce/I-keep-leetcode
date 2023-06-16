class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        ans = [0, 0]
        while l < r:
            if numbers[l] + numbers[r] == target:
                ans = [l+1, r+1]
                return ans #!!! it's ok because there is only 1 solution
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1