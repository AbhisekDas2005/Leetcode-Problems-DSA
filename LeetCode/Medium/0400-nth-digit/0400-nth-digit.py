class Solution:
    def findNthDigit(self, n: int) -> int:
        d=1
        s=1
        while True:
            c=9 * s
            block=c*d
            if n>block:
                n-=block
                d+=1
                s*=10
            else:
                break
        number=s+(n-1)//d
        index =(n-1)%d
        return int(str(number)[index])