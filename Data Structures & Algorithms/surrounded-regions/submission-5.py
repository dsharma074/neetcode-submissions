# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         oset = set()
#         row = len(board)
#         col = len(board[0])
#         q = []

#         for i in range(row):
#             if board[i][0]== "O":
#                 q.append([i,0])
#             if board[i][col-1]=="O":
#                 q.append([i,col-1])
#         for i in range(col):
#             if board[0][i]== "O":
#                 q.append([0,i])
#             if board[row-1][i]=="O":
#                 q.append([row-1,i])
#         dir = [[-1,0],[1,0],[0,1],[0,-1]]
#         # print(q)
#         i = 0
#         while i < len(q):
#             x,y = q[i]
#             oset.add((x,y))
#             for dr, dc in dir:
#                 r = x + dr
#                 c = y + dc
#                 if 0<=r< row and 0<=c<col and (r,c) not in oset and board[r][c] =="O":
#                     q.append([r,c])
#                     oset.add((r,c))
#             i += 1
#         # print(oset)
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if (i,j) not in oset:
#                     board[i][j] = "X"
#         return 


from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        row = len(board)
        col = len(board[0])

        q = deque()

        for i in range(row):
            if board[i][0] == "O":
                q.append((i, 0))
                board[i][0] = "T"

            if board[i][col - 1] == "O":
                q.append((i, col - 1))
                board[i][col - 1] = "T"

        for j in range(col):
            if board[0][j] == "O":
                q.append((0, j))
                board[0][j] = "T"

            if board[row - 1][j] == "O":
                q.append((row - 1, j))
                board[row - 1][j] = "T"

        dir = [[-1,0], [1,0], [0,1], [0,-1]]

        while q:
            x, y = q.popleft()

            for dr, dc in dir:
                r = x + dr
                c = y + dc

                if (
                    0 <= r < row
                    and 0 <= c < col
                    and board[r][c] == "O"
                ):
                    board[r][c] = "T"
                    q.append((r, c))

        for i in range(row):
            for j in range(col):

                if board[i][j] == "O":
                    board[i][j] = "X"

                elif board[i][j] == "T":
                    board[i][j] = "O"

