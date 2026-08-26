class Solution:
    def solve(self, board: List[List[str]]) -> None:
        oset = set()
        row = len(board)
        col = len(board[0])
        q = []

        for i in range(row):
            if board[i][0]== "O":
                q.append([i,0])
            if board[i][col-1]=="O":
                q.append([i,col-1])
        for i in range(col):
            if board[0][i]== "O":
                q.append([0,i])
            if board[row-1][i]=="O":
                q.append([row-1,i])
        dir = [[-1,0],[1,0],[0,1],[0,-1]]
        # print(q)
        i = 0
        while i < len(q):
            x,y = q[i]
            oset.add((x,y))
            for dr, dc in dir:
                r = x + dr
                c = y + dc
                if 0<=r< row and 0<=c<col and (r,c) not in oset and board[r][c] =="O":
                    q.append([r,c])
            i += 1
        # print(oset)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in oset:
                    board[i][j] = "X"
        return 




