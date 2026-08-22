class Solution:
    def countBits(self, n: int) -> List[int]:
        a=[]
        for i in range(n+1):
            n=i
            c=0
            while(n>0):
                if n%2==1:
                    c+=1
                n//=2
            a.append(c)
        return a
        