class Solution:
    def gcd(self,a, b):
        while b != 0:
            a, b = b, a % b
        return a
    def gcdSum(self, nums: list[int]) -> int:
        li=[]
        mx=float('-inf')
        for i in nums:
            if i >mx:
                mx=i
            li.append(self.gcd(i,mx))
        li.sort()
        a=0
        l,r=0,len(li)-1
        while l<r:
            a+=self.gcd(li[l],li[r])
            l+=1
            r-=1
        return a
    
            

        