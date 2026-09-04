class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        pn=[]
        for i in range(len(nums)):
            pn.append(nums[i])
            ins=max(pn)-min(nums[i:])
            if ins<=k:
                return i
        else:
            return -1
        