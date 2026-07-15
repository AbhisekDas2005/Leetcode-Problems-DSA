class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        li=[]
        for i in matrix:
            for j in i:
                li.append(j)
        l=0
        print(li)
        r=len(li)
        while l<r:
            mid=(l+r)//2
            if target==li[mid]:
                return True
            elif target<li[mid]:
                r-=1
            else:
                l+=1
        return False


        