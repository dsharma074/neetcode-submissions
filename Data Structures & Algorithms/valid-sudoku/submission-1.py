class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        def box_val(i,j):
            return (i//3)*3 + j//3
        
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]==".":
                    continue
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in box[box_val(i,j)]:
                    return False
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                box[box_val(i,j)].add(board[i][j])
        return True

                
        