class Solution:
    def addDigits(self, num: int) -> int:
        a=0
        while num>=10:
            a=0
            for i in str(num):
                a+=int(i)
            num=a
        return num