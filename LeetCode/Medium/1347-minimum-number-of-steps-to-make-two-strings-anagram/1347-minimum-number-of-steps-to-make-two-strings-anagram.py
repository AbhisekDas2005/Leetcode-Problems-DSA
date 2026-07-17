class Solution:
    def minSteps(self, s: str, t: str) -> int:
        f1=Counter(s)
        f2=Counter(t)
        ts=0
        for i in f1:
             if f1[i] > f2[i]:
                ts+=f1[i]-f2[i]
        return ts
        