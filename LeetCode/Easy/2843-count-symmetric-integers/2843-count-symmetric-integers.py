class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for x in range(low, high + 1):
            s=str(x)
            if len(s)%2!=0:
                continue
            n=len(s)//2
            ls=sum(int(d) for d in s[:n])
            rs=sum(int(d) for d in s[n:])
            if ls==rs:
                count += 1
        return count