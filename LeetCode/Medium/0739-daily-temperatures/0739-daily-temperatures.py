class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l=[0]*len(temperatures)
        s=[]#pair of temp then index
        for i,t in enumerate(temperatures):
            while s and t>s[-1][0]:
                stemp,sindex=s.pop()
                l[sindex]=(i-sindex)
            s.append([t,i])
        return l
            



        