class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k!=0:
            n=min(nums)
            nums[nums.index(n)]=multiplier*n
            k-=1
        return nums
        