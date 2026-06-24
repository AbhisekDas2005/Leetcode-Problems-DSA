class Solution:
    def minCost(self, n: int) -> int:
        s={}
        def split(x):
            if x==1:
                return 0
            if x in s:
                return s[x]
            ans = float('inf')
            for a in range(1, x//2 + 1):
                b=x-a
                ans=min(ans,a*b+split(a)+split(b))
            s[x]=ans
            return ans
        return split(n)