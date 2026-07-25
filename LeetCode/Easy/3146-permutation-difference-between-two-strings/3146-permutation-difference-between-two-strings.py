class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        a=0
        for i in range(len(s)):
            a+=abs(i-t.find(s[i]))
        return a
        