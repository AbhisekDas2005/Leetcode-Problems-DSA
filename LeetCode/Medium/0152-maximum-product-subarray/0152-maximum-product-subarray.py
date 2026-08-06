class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxn,minn=nums[0],nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            n=nums[i]
            if n<0:
                maxn,minn=minn,maxn
            maxn=max(n,maxn*n)
            minn=min(n,minn*n)
            res=max(res,maxn)
        return res

            