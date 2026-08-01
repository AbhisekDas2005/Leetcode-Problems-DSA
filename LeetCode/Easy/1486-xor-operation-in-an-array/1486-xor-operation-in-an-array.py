class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        a=0
        for i in range(n):
            a^=start+2*i
        return a
        