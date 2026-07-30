class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        l=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        a=[]
        for i in words:
            s=""
            for j in i:
                s+=l[ord(j.lower())-97]
            if s not in a:
                a.append(s)
        return len(a)
        