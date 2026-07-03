class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        f1=Counter(s1)
        f2=Counter(s2[:len(s1)])
        if f1==f2:
            return True
        l=0
        r=len(s1)
        while r<len(s2):
            f2[s2[l]]-=1
            if f2[s2[l]]==0:
                del f2[s2[l]]
            f2[s2[r]]+=1
            l+=1
            r+=1
            if f1==f2:
                return True
        return False