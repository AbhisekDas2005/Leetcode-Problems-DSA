class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        d=dict(sorted(c.items(), key=lambda item: item[1], reverse=True))
        l=[]
        for i in range(k):
            l.append(list(d)[i])
        return l
        