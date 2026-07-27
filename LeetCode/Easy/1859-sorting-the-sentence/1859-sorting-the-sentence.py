class Solution:
    def sortSentence(self, s: str) -> str:
        a = s.split(" ")
        l = [""]*len(a)
        for i in a:
            l[int(i[-1])-1]=i[:-1]
        return " ".join(l)