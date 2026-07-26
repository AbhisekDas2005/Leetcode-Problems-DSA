class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        f1=Counter(nums1)
        f2=Counter(nums2)
        a,b=0,0
        for i in f1:
            if i in f2:
                a+=f1[i]
                b+=f2[i]
        return [a,b]