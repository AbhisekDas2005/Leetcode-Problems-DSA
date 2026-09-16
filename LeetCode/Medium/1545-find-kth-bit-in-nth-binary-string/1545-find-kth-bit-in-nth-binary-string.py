class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse(s: str) -> str:
            return s[::-1]
        def invert(s: str) -> str:
            return "".join("1" if bit == "0" else "0" for bit in s)
        def generatestring(n: int) -> str:
            if n==1:
                return "0"
            prev=generatestring(n - 1)
            return prev+"1"+reverse(invert(prev))
        a=generatestring(n)
        return a[k - 1]