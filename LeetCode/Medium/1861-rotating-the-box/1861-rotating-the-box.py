class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        for i in boxGrid:
            empty = len(i) - 1
            for j in range(len(i)-1, -1, -1):
                if i[j] == '*':
                    empty = j - 1
                elif i[j] == '#':
                    i[j] = '.'
                    i[empty] = '#'
                    empty-=1
        a=[]
        for i in range(len(boxGrid[0])):
            l=[]
            j=len(boxGrid)-1
            while j>=0:
                l.append(boxGrid[j][i])
                j-=1
            a.append(l)
        return a
            


        