class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l=[]
        for i in range(n):
            l.append(i+1)
        idx = 0
        while len(l) > 1:
            idx = (idx + k - 1) % len(l)
            l.pop(idx)
        return l[0]

        