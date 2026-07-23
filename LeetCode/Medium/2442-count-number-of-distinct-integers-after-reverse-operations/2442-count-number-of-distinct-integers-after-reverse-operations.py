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

        #solution 2(attempted??)
        # c = 0
        # s = []
        # for i in nums:
        #     rev = int(str(i)[::-1])
        #     if i not in s:
        #         s.append(i)
        #         c += 1
        #     if rev not in s:
        #         s.append(rev)
        #         c += 1
        # return c