class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if len(str(i))==1:
                l.append(i)
            else:
                l.append(int(str(i)[::-1]))
        nums.extend(l)
        return(len(set(nums)))
        # c=0
        # s=[]
        # for i in nums:
        #     if len(str(i))==1 and str(i) not in s:
        #         c+=1
        #         s.append(int(str(i)))
        #     else:
        #         if str(i)==str(i)[::-1] and int(str(i)) not in s:
        #             c+=1
        #         else:
        #             if int(str(i)) not in s:
        #                 c+=1
        #             if int(str(i)[::-1]) not in s:
        #                 c+=1
        # return c
        