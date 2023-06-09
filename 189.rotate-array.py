from typing import List
class Solution:
    # Method 1: use O(n) space
    def rotate1(self, nums: List[int], k: int) -> None:
        rnums = nums[:] #!!!
        n = len(nums)
        for i in range(0, n):
            nums[(i+k)%n] = rnums[i]
        return 
    # Method 2: use O(1) space
    # TODO: try to reverse nums in a Pythonic way
    def reverse(self, nums: List[int], l: int, r: int) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    def rotate2(self, nums: List[int], k: int) -> None:
        k = k % n #!!! handle cases where len(nums) < k
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
    # Method 3: use O(1) space
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next = (current + k) % n
                nums[next], prev = prev, nums[next]
                current = next
                count += 1
                
                if start == current:
                    break
            start += 1
            
                
        