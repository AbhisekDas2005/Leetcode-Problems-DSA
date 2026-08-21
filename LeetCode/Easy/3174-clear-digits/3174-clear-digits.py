class Solution:
    def clearDigits(self, s: str) -> str:
        l=[]
        for i in s:
            if i not in '1234567890':
                l.append(i)
            else:
                l.pop()
        return "".join(l)
            
        