from typing import List
class Solution:
    #写的第一个方法，it works,但time complexity并不是严格意义上的o(logn)
    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)-1
        if j == -1:
            return [-1,-1]
        while i <= j:
            mid = i + (j-i)//2
            if nums[mid] > target:
                j = mid - 1
            elif nums[mid] < target:
                i = mid + 1
            else: 
                i = j + 1
        left, right = -1, -1
        if nums[mid] == target:
            left, right = mid, mid
            while(left-1>=0 and nums[left-1]==target):
                left -= 1
            while(right+1<len(nums) and nums[right+1]==target):
                right += 1
        return [left, right]
    #更符合要求的写法是：使用两次二分
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l,r = 0,n-1
        ans = [-1,-1]
        if n == 0:
            return ans
        #寻找左边界
        while(l<r): # while(l<r)
            mid = (l+r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        ans[0] = (r if nums[r]==target else -1)
        #寻找右边界
        l,r = 0,n-1
        while(l<r):
            mid = (l+r+1)>>1 
            if nums[mid] <= target:
                l = mid 
            else:
                r = mid -1
        ans[1] = (r if nums[r]==target else -1)
        return ans
            
        

solution = Solution()
ans = solution.searchRange([1, 2,2,2,3,3,3,3,3,3,3,3,34], 2)
print(ans)