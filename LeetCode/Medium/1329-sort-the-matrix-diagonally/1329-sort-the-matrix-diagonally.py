class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        
        for i in range(n): # for col
            x,y=0,i
            temp=[]
            while x<m and y<n:
                temp+=[mat[x][y]]
                x+=1
                y+=1

            temp.sort()
            x,y=0,i
            for el in temp:
                mat[x][y]=el
                x+=1
                y+=1

        for j in range(m): # for row
            x,y=j,0
            temp=[]
            while x<m and y<n:
                temp+=[mat[x][y]]
                x+=1
                y+=1

            temp.sort()
            x,y=j,0
            for el in temp:
                mat[x][y]=el
                x+=1
                y+=1

        return mat

        
        