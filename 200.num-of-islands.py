class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    num += 1
        return num
    def dfs(self, grid: List[List[str]], r: int, c: int):
        grid[r][c] = "0"
        nr = len(grid)
        nc = len(grid[0])
        for x,y in [(r-1,c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                

                