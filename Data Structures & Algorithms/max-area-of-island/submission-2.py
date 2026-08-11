class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        row = len(grid)
        col = len(grid[0])
        area = max(max(grid))
        dir = [[-1,0],[0,-1],[1,0],[0,1]]

        for i in range(row):
            for j in range(col):
                if (i,j) not in visited and grid[i][j] == 1:
                    localarea = 0
                    stack = [[i,j]]
                    while stack:
                        r,c = stack.pop()
                        for dr, dc in dir:
                            if 0 <= r+dr < row and 0 <= c+dc < col and grid[r+dr][c+dc] == 1 and (r+dr,c+dc) not in visited:
                                stack.append([r+dr, c+dc])
                                localarea += 1
                                visited.add((r+dr,c+dc))
                    area = max(area, localarea)
                visited.add((i,j))
        
        return area