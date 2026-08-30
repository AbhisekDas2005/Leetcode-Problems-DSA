class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        l=len(nums)
        minl=nums.index(min(nums))
        maxl=nums.index(max(nums))
        front=max(minl, maxl)+1
        back=l-min(minl, maxl)
        mixed1=minl+1+(l - maxl)
        mixed2 =maxl+1+(l - minl)

        return min(front, back, mixed1, mixed2)