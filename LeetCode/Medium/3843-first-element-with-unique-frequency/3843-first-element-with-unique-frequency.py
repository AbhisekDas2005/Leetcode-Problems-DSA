class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        f=Counter(nums)
        freq_count=Counter(f.values())
        for num in nums:
            if freq_count[f[num]] == 1:
                return num
        return -1
        