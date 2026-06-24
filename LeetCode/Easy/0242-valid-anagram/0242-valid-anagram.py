class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            f1=Counter(s)
            f2=Counter(t)
            for i in s:
                if f1[i]!=f2[i]:
                    return False
            else:
                return True
        else:
            return False
        

        