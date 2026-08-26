class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificset = set()
        q = []
        row = len(heights)
        col = len(heights[0])
        for i in range(col):
            q.append([0,i])
        for i in range(row):
            q.append([i,0])
        dir = [[-1,0],[1,0],[0,-1],[0,1]]
        i = 0
        while i < len(q):
            x,y = q[i]
            pacificset.add((x,y))
            for dr, dc in dir:
                r = x+dr
                c = y+dc
                if 0<=r<row and 0<=c<col and heights[r][c] >= heights[x][y]  and (r,c) not in pacificset:
                    q.append([r,c])
            i += 1
        

        atlanticset = set()
        q = []
        for i in range(col):
            q.append([row-1,i])
        for i in range(row):
            q.append([i,col-1])
        dir = [[-1,0],[1,0],[0,-1],[0,1]]
        i = 0
        while i < len(q):
            x,y = q[i]
            atlanticset.add((x,y))
            for dr, dc in dir:
                r = x+dr
                c = y+dc
                if 0<=r<row and 0<=c<col and heights[r][c] >= heights[x][y]  and (r,c) not in atlanticset:
                    q.append([r,c])
            i += 1

        finalset = atlanticset.intersection(pacificset)
        # print(row,col)
        # print(atlanticset)
        # print(pacificset)

        return list(finalset)


        