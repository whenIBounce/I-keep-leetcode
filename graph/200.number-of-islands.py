class Solution:
    # dfs
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        row, col = len(grid), len(grid[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        res = 0

        def traverse(i, j):
            visited.add((i, j))

            for direction in directions:
                n_i, n_j = i+direction[0], j+direction[1]
                if n_i >= 0 and n_i < row and n_j >= 0 and n_j < col:
                    if grid[n_i][n_j] == '1' and (n_i, n_j) not in visited:
                        traverse(n_i, n_j)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and (r, c) not in visited:
                    res = res + 1
                    traverse(r, c)

        return res
