class Solution:
    def reverseParentheses(self, s: str) -> str:
        l=[]
        for i in s:
            if i !=')':
                l.append(i)
            else:
                s=''
                while l[len(l)-1]!='(':
                    s+=l.pop()
                print(s)
                l.pop()
                for j in s:
                    l.append(j)
        return ",".join(l).replace(",","")

        