class Solution:
    def isHappy(self, n: int) -> bool:
        l=[]
        s=str(n)
        a=0
        while a!=1:
            a=0
            for i in s:
                a+=(int(i)**2)
            if a in l:
                return False
            else:
                l.append(a)
            s=str(a)
        return True