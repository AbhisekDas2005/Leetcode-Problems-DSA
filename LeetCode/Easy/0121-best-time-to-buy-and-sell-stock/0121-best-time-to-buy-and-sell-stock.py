class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        minp=float(inf)
        for i in prices:
            if i <minp:
                minp=i
            elif i>minp:
                if (i-minp)>maxp:
                    maxp=i-minp
            else:
                continue
        return maxp
        