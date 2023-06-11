from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h = 0
        for i in range(len(citations)-1, -1, -1):
            if citations[i] > h:
                h += 1
            else:
                break
        return h

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
