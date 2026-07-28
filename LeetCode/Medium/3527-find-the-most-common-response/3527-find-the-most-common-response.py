class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        d={}
        a=[]
        for i in responses:
            a.append(set(i))
        for i in a:
            for j in i:
                if j not in d:
                    d[j]=1
                else:
                    d[j]+=1
        return min(d.items(), key=lambda x: (-x[1], x[0]))[0]

            
                    
            
            