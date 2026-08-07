class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        f=Counter(s)
        fs=""
        if f['1']>=1:
            fs+="1"
            f["1"]-=1
        else:
            return s
        fs=f['1']*'1'+ f['0']*'0'+fs
        return fs