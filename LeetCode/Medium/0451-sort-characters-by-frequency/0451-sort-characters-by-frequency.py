class Solution:
    def frequencySort(self, s: str) -> str:
        f=Counter(s)
        f=dict(sorted(f.items(), key=lambda item: item[1], reverse=True))
        ns=""
        for i in f:
            ns+=f[i]*i
        return ns
        