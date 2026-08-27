class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        onerow=[]
        zerorow=[]
        for i in grid:
            f=i.count(1)
            onerow.append(f)
            zerorow.append(n-f)
        onecol=[]
        zerocol=[]
        for j in range(n):
            count=0
            for i in range(m):
                    if grid[i][j]==1:
                        count+=1
            onecol.append(count)
            zerocol.append(m-count)
        for i in range(m):
            for j in range(n):
                grid[i][j]=onerow[i]+onecol[j]-zerorow[i]-zerocol[j]
        return grid
