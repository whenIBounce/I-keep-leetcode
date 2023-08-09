from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        l, r = 0, n-1
        #套用二分查找，寻找左边界的模版
        while(l<r):
            mid = (l+r) >> 1
            if citations[mid] >= n-mid:
                r = mid
            else:
                l = mid + 1
        return min(citations[r],n-r)

s = Solution()

# Test Case 1:
citations1 = [3, 0, 6, 1, 5]
print(s.hIndex(citations1))  # Output should be 3

# Test Case 2:
citations2 = [1, 3, 1]
print(s.hIndex(citations2))  # Output should be 1

# Test Case 3:
citations3 = [1, 2, 100]
print(s.hIndex(citations3))  # Output should be 2

citations4 = [0]
print(s.hIndex(citations4))
