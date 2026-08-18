class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ds=0
        es=0
        for i in nums:
            es+=i
            if len(str(i))==1:
                ds+=i
            else:
                ds+=sum(int(x) for x in str(i))
        return int(math.fabs(es-ds))