class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        m=float("inf")
        for i in tasks:
            s=i[0]+i[1]
            if s<m:
                m=s
        return m
        