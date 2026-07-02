class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        maxl=0
        freq=[0]*26
        for r in range(len(s)):
            freq[ord(s[r])-65]+=1
            while (r-l)+1-max(freq)>k:
                freq[ord(s[l])-65]-=1
                l+=1
            maxl=max(maxl,(r-l+1))
        return maxl


