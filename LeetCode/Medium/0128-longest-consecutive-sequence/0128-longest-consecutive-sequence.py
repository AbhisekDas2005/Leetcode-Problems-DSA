class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        c=0
        m=0
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                c+=1
                if m<c:
                    m=c
            elif nums[i]==nums[i+1]:
                continue
            else:
                c=0
        return m+1