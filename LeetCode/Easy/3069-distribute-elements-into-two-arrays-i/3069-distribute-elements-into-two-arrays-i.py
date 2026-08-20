class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a1=[]
        a2=[]
        for i in range(len(nums)):
            if i==0:
                a1.append(nums[i])
            elif i==1:
                a2.append(nums[i])
            else:
                if a1[-1]>a2[-1]:
                    a1.append(nums[i])
                else:
                    a2.append(nums[i])
        return a1+a2