class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        dir = [[-1,0],[0,-1],[1,0],[0,1]]
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in visited:
                    visited.add((i,j))
                    count +=1
                    
                    stack = [[i,j]]
                    while stack:
                        r,c = stack.pop()
                        for dr,dc in dir:
                            if 0 <= r+dr < row and 0 <= c+dc < col and grid[r+dr][c+dc] == "1" and (r+dr, c+dc) not in visited:
                                visited.add((r+dr,c+dc))
                                stack.append([r+dr, c+dc])
                visited.add((i,j))

        return count

        