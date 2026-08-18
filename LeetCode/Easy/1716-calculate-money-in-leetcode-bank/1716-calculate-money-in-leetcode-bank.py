class Solution:
    def totalMoney(self, n: int) -> int:
        d=0
        w=0
        total=0
        for i in range(1,n+1):
            if d==7:
                d=0
                w+=1
            total+=(i-1)%7+1+w
            d+=1
        return total
        