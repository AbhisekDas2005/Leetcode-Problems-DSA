class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        d1=0
        d2=0
        for i in range(n):
            d1+=mat[i][i]
            d2+=mat[i][n-i-1]
        if n%2==1:
            d2-=mat[n//2][n//2]
        return d1+d2
        