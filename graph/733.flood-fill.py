class Solution:
    # dfs
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image

        visited = set()
        row, col = len(image), len(image[0])
        directions = ((-1,  0), (1, 0), (0, -1), (0, 1))

        def traverse(i, j):
            if (i, j) in visited:
                return
            visited.add((i, j))

            for direction in directions:
                n_i, n_j = i+direction[0], j+direction[1]
                if n_i >= 0 and n_i < row and n_j >= 0 and n_j < col:
                    if image[n_i][n_j] == image[i][j]:
                        traverse(n_i, n_j)

        traverse(sr, sc)

        for (vr, vc) in visited:
            image[vr][vc] = color

        return image
