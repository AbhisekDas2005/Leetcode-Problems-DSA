class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        l=0
        r=len(nums)//2
        for i in range(len(nums)):
            if i%2==0:
                ans.append(nums[l])
                l+=1
            else:
                ans.append(nums[r])
                r+=1
        return ans       

                
        