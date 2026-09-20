class Solution:
    def arraySign(self, nums: list[int]) -> int:
        flag=True
        for i in nums:
            if i==0:
                return 0
            elif i<0:
                flag=not(flag)
            else:
                continue
        if(flag):
            return 1
        else:
            return -1

        