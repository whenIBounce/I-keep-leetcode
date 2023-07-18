class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        max_area = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j)
                    max_area = max(area, max_area)
        return max_area
    def dfs(self, grid: List[List[int]], r: int, c:int) -> int:
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
            return 0
        area = 1
        grid[r][c] = 0
        for x,y in [(r-1,c),(r+1,c),(r, c-1),(r,c+1)]:
            area += self.dfs(grid, x, y)
        return area