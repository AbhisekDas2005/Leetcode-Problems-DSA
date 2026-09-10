class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        s=""
        while(n>0):
            s=str(n%3)+s
            n//=3
        print(s)
        if '2'in s:
            return False
        else:
            return True