class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in points:
            distances.append((i[0]**2 + i[1]**2, i))
        distances.sort(key=lambda x: x[0])
        return [point for distance, point in distances[:k]]