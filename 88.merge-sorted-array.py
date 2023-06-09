from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        for i in range(len(nums1)-1,-1,-1):
            if p1 == -1 and p2 != -1:
                nums1[i] = nums2[p2]
                p2 -= 1
            elif p2 == -1 and p1 != -1:
                nums1[i] = nums1[p1]
                p1 -= 1
            elif nums2[p2] >= nums1[p1]:
                nums1[i] = nums2[p2]
                p2 -= 1
            else:
                nums1[i] = nums1[p1]
                p1 -= 1
        return 

# Initialize the class
solution = Solution()

# Create some test cases
test_cases = [
    ([1,2,3,0,0,0], 3, [2,5,6], 3),  # Expects [1,2,2,3,5,6]
    ([0], 0, [1], 1),  # Expects [1]
    # Add more test cases as needed
]

# Run the test cases
for nums1, m, nums2, n in test_cases:
    solution.merge(nums1, m, nums2, n)
    print(nums1)