class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        c=0
        valid=True
        for i in text:
            if i == ' ':
                if valid:
                    c+=1
                valid=True
            elif i in brokenLetters:
                valid=False
        if valid:
            c+=1
        return c