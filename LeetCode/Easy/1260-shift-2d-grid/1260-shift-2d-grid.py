class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n=len(grid)
        m=len(grid[0])
        l= [[0 for _ in range(m)] for _ in range(n)]
        while(k!=0):
            for i in range(n):
                for j in range(m):
                   if i == n-1 and j == m-1:
                        l[0][0] = grid[i][j]
                   elif j == m-1:
                        l[i+1][0] = grid[i][j]
                   else:
                        l[i][j+1] = grid[i][j]
            grid=l
            l= [[0 for _ in range(m)] for _ in range(n)]
            k-=1
        return grid


