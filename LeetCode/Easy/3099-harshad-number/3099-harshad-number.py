class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        l=[]
        for i in str(x):
            l.append(int(i))
        if x%sum(l)==0:
            return sum(l)
        return -1
        