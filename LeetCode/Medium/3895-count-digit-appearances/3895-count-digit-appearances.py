class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        d=str(digit)
        c=0
        for i in nums:
            for j in str(i):
                if j==d:
                    c+=1
        return c
        