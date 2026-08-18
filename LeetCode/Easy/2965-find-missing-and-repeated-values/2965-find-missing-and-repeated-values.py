class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l=[]
        d=-1
        lens=len(grid)
        for i in grid:
            for j in i:
                if j in l:
                    d=j
                else:
                    l.append(j)
        nf=-1
        for i in range(1,(lens**2)+1):
            if i not in l:
                nf=i
        return [d,nf]
        