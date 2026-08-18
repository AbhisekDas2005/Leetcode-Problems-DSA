class Solution:
    def replaceDigits(self, s: str) -> str:
        l=[]
        for i in s:
            if i.isalpha():
                l.append(i)
            else:
                c=chr(ord(l[-1])+int(i))
                l.append(c)
        return "".join(l)
        