class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        a=0
        for i in range(1,n//8 +1):
            a+=8*i
        a+=(n%8)*((n//8)+1)
        return a
