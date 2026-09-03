class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1=s1.split(" ")
        l2=s2.split(" ")
        a=set(l1)
        b=set(l2)
        se3=(a.union(b)).difference(a.intersection(b))
        l=[]
        f1=Counter(l1)
        f2=Counter(l2)
        for i in se3:
            if i in f1 and f1[i]!=1:
                continue
            if i in f2 and f2[i]!=1:
                continue
            else:
                l.append(i)

        return l