class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        l=[]
        for i in nums:
            if i%k==0:
                l.append(i/k)
        c=1
        while(True):
            if c not in l:
                return c*k
            else:
                c+=1
            
        