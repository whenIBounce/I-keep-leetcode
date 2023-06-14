from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1 for _ in range(n)]
        right = [1 for _ in range(n)]
        # 满足左规则
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1           
        # 满足右规则
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] + 1
        total = 0
        for i in range(0, n):
            total += max(left[i], right[i])
        return total
s = Solution()
ratings = [3,2,1,5,4,3,2,0]
print(s.candy(ratings))