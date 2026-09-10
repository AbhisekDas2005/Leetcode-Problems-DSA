class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False
        f=1
        i=2
        while(i*i<=num):
            if(num%i==0):
                f+=i
                f+=num/i
            i+=1
        if(f==num):
            return True
        else:
            return False
        
        