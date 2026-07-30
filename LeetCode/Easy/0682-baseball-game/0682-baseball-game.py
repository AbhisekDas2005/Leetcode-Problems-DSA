class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l=[]
        for i in operations:
            if i not in "+DC":
                l.append(int(i))
            elif i=="+":
                n=int(l[-1])+int(l[-2])
                l.append(n)
            elif i=='D':
                n=2*int(l[-1])
                l.append(n)
            else:
                l.pop()
        return sum(l)