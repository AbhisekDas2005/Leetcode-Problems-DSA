class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ns=""
        for i in words:
            s=0
            for j in i:
                s+=weights[ord(j)-97]
            s=s%26
            ns+=chr(ord('z')-s)
        return ns
            
        