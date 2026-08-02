class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        t,f=0,0
        r,c,=len(grid),len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    f+=1
                if grid[i][j]==2:
                    q.append([i,j])
        dir=[[0,1],[0,-1],[1,0],[-1,0]]
        while q and f>0:
            for i in range(len(q)):
                  a,b=q.popleft()
                  for dr,dc in dir:
                    row,col=dr+a,dc+b
                    if(row<0 or row==len(grid) or col<0 or col==len(grid[0]) or grid[row][col]!=1):
                        continue
                    grid[row][col]=2
                    q.append([row,col])
                    f-=1
            t+=1
        return t if f==0 else -1