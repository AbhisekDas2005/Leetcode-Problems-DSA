class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        f=Counter(nums)
        l=[]
        for i in f:
            if f[i]==2:
                l.append(i)
        return l