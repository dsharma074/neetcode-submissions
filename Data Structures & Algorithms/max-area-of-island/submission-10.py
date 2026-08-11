# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         visited = set()
#         row = len(grid)
#         col = len(grid[0])
#         area = 0
#         dir = [[-1,0],[0,-1],[1,0],[0,1]]

#         for i in range(row):
#             for j in range(col):
#                 if (i,j) not in visited and grid[i][j] == 1:
#                     localarea = 0
#                     stack = [[i,j]]
                    
#                     while stack:
#                         r,c = stack.pop()
#                         localarea += 1
#                         visited.add((r,c))
#                         for dr, dc in dir:
#                             if 0 <= r+dr < row and 0 <= c+dc < col and grid[r+dr][c+dc] == 1 and (r+dr,c+dc) not in visited:
#                                 stack.append([r+dr, c+dc])
#                             visited.add((r+dr,c+dc))
#                     area = max(area, localarea)
#                 # visited.add((i,j))
        
#         return area


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        max_area = 0

        directions = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 1:

                    stack = [(i, j)]
                    grid[i][j] = 0

                    local_area = 0

                    while stack:
                        r, c = stack.pop()
                        local_area += 1

                        for dr, dc in directions:
                            nr = r + dr
                            nc = c + dc

                            if (
                                0 <= nr < rows
                                and 0 <= nc < cols
                                and grid[nr][nc] == 1
                            ):
                                grid[nr][nc] = 0
                                stack.append((nr, nc))

                    max_area = max(max_area, local_area)

        return max_area