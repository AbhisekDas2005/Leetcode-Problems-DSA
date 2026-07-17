class Solution:
    def sums(self,n):
        if len(n)==1:
            return n[0]
        l=[]
        for i in range(len(n)-1):
            l.append((n[i]+n[i+1])%10)
        return self.sums(l)

    def triangularSum(self, nums: List[int]) -> int:
        return self.sums(nums)
        