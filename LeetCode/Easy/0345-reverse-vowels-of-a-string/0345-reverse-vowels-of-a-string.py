class Solution:
    def reverseVowels(self, s: str) -> str:
        v=[]
        for i in s:
            if i in "AEIOUaeiou":
                v.append(i)
        a=''
        for i in s:
            if i in "AEIOUaeiou":
                a+=v[-1]
                v.pop()
            else:
                a+=i
        return a