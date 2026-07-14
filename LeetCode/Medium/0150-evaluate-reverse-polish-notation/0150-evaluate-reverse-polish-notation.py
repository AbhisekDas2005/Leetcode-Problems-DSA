class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=[]
        for i in tokens:
            if i not in "+-*/":
                l.append(int(i))
            if i in "+-*/":
                b=int(l.pop())
                a=int(l.pop())
                match(i):
                    case "+":
                        s=a+b
                        l.append(s)
                    case"-":
                        s=a-b
                        l.append(s)
                    case "*":
                        s=a*b
                        l.append(s)
                    case"/":
                        s=int(a/b)
                        l.append(s)
        return l[0]    
        

        