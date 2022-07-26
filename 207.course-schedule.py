from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
pre = [[1,0],[1,2],[0,1]]
print(Solution().canFinish(numCourses, pre))
