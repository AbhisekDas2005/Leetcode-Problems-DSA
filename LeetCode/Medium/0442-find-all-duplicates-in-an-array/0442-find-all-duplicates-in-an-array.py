class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # l=[]
        # s=[]
        # for i in nums:
        #     if i in l:
        #         s.append(i)
        #     else:
        #         l.append(i)
        # return s
        
        freq=Counter(nums)
        l=[]
        for i in freq:
            if freq[i]!=1:
                l.append(i)
        return l