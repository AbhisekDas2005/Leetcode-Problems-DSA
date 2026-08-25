class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s=set(nums)
        c=1
        while(True):
            if c*k not in s:
                return c*k
            else:
                c+=1
            
        