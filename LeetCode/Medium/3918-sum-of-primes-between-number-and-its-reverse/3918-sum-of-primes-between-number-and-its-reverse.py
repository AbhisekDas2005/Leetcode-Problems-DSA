class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        s=0
        for i in range(min(n,int(str(n)[::-1])),max(n,int(str(n)[::-1]))+1):
            if i==1:
                continue
            if i==2:
                s+=2
                continue
            for j in range(2,i//2+1):
                if i%j==0:
                    break
            else:
                print(i)
                s+=i
        return s
        