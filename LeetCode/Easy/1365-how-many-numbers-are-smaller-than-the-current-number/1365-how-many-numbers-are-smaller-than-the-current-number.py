class Solution:
    def smallerNumbersThanCurrent(self,nums):
        sorted_nums=sorted(nums)
        first={}
        for i, num in enumerate(sorted_nums):
            if num not in first:
                first[num]=i
        return [first[num] for num in nums]            
        