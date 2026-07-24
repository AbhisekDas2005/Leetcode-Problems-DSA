class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        s=0
        for i in range(min(n, int(str(n)[::-1])), max(n, int(str(n)[::-1])) + 1):
            if i < 2:
                continue

            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    break
            else:
                s += i
        return s
        