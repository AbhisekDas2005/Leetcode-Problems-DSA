class Solution(object):
    def reverse(self, x):
        neg=x<0
        x=abs(x)
        rx=int(str(x)[::-1])
        if neg:
            rx=-rx
        if rx<-2**31 or rx>2**31 - 1:
            return 0
        return rx