class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        st=0
        cc=capacity
        for i in range(len(plants)):
            if cc < plants[i]:
                st += 2*i
                cc = capacity
            st += 1
            cc -= plants[i]
        return st


        