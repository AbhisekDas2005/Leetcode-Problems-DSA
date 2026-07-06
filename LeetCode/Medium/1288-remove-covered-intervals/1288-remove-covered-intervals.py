class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], -x[1]))
        m=float("-inf")
        c=0
        for i in range(len(intervals)):
            if intervals[i][1]>m:
                m=intervals[i][1]
                c+=1
        return c
             