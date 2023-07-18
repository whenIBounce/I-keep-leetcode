from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        cur_pos = len(nums1) - 1
        while  p2 >= 0:
            if p1 == -1:
                nums1[cur_pos] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[cur_pos] = nums1[p1]
                p1 -= 2
            elif nums2[p2] >= nums1[p1]:
                nums1[cur_pos] = nums2[p2]
                p2 -= 1
            else:
                nums1[cur_pos] = nums1[p1]
                p1 -= 1
            cur_pos -= 1
        print(nums1)

num1 = [1, 2, 3, 0, 0, 0]
num2 = [2, 5, 6]
s = Solution()
s.merge(num1, 3, num2, 3)