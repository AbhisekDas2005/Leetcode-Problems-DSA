class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        f=Counter(words)
        f=sorted(f.items(),key=lambda item:(-item[1],item[0]))
        l=[]
        c=0
        for i in f:
            if c==k:
                break
            else:
                l.append(i[0])
                c+=1
        return l