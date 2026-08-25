class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        row = len(grid)
        col = len(grid[0])
        q = deque()
        freshcount = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append([i,j])
                elif grid[i][j] == 1:
                    freshcount += 1
        i = 0
        min = 0
        dir = [[-1,0],[1,0],[0,1],[0,-1]]
        if not q and freshcount ==0:
            return 0
        while q:
            for _ in range(len(q)):
                x,y = q.popleft()
                for dr, dc in dir:
                    r = x+dr
                    c = y+dc
                    if 0<=r<row and 0<=c<col and grid[r][c] == 1:
                        q.append([r,c])
                        grid[r][c] = 2
                        freshcount -= 1
            min += 1
 
        if freshcount !=0:
            return -1
        return min-1
