class Solution:
    # bfs
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = ((-1,  0), (1, 0), (0, -1), (0, 1))
        row, col = len(mat), len(mat[0])
        queue = deque([])

        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1

        while(queue):
            i, j = queue.popleft()
            for direction in directions:
                ni, nj = i+direction[0], j+direction[1]
                if ni >= 0 and ni < row and nj >= 0 and nj < col:
                    if mat[ni][nj] == -1:
                        mat[ni][nj] = mat[i][j] + 1
                        queue.append((ni, nj))

        return mat
