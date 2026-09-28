class Solution:
    def factorial(self, a:int):
        if a==1 or a==0:
            return 1
        else:
            return(a*self.factorial(a-1))
    def getRow(self, rowIndex: int) -> List[int]:
        l=[]
        for i in range(rowIndex+1):
            v= (self.factorial(rowIndex)//(self.factorial(i)*self.factorial(rowIndex-i)))
            l.append(v)
        return l