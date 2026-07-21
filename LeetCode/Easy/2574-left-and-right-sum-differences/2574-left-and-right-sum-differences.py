class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(0,len(nums)):
            l=sum(nums[:i])
            r=sum(nums[i+1:])
            a.append(abs(l-r))
        return a
        