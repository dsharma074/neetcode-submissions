class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        row = len(grid)
        col = len(grid[0])
        visited = set()
        dir = [[-1,0],[1,0], [0,-1],[0,1]]
        q = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append([i,j])
            

        while q:
            x,y = q.popleft()
            visited.add((x,y))
            for dr, dc in dir:
                r = x+dr
                c = y+dc
                if 0<=r<row and 0<=c<col and (r,c) not in visited and grid[r][c] != -1 and grid[r][c] != 0: 
                    grid[r][c] = grid[x][y]+1
                    q.append([r,c])
                    visited.add((r,c))

        return




                    
                    




