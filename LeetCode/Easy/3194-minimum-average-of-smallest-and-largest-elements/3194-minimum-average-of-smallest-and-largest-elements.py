class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        l=[]
        for i in range(len(nums)//2):
            a=min(nums)
            b=max(nums)
            nums.remove(a)
            nums.remove(b)
            l.append((a+b)/2)
        return min(l)
