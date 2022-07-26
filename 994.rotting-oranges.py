from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        minRottenTime = 0
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        q = deque()
        stillFresh = 0 
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    grid[r][c] = 0 #initially rotten orange time: 0
                    q.append((r, c))
                elif (grid[r][c] == 1):
                    grid[r][c] = -1 #use -1 to mark fresh oranges
                    stillFresh += 1
                else:
                    grid[r][c] = -2 #special char for empty cell
        
        while(q):
            r, c = q.popleft()
            for d in directions:
                nr, nc = r+d[0], c+d[1]
                if nr >= 0 and nc >= 0 and nr < m and nc < n:
                    if grid[nr][nc] == -1:
                        stillFresh -= 1
                        grid[nr][nc] = grid[r][c] + 1
                        minRottenTime = grid[nr][nc] if grid[nr][nc] > minRottenTime else minRottenTime
                        q.append((nr, nc))
        
        return minRottenTime if stillFresh == 0 else -1
