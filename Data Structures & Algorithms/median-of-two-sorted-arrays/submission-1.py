class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        big = nums1 + nums2
        big.sort()

        if len(big) % 2 == 1:
            return float(big[len(big) // 2])

        if len(big) % 2 == 0: 
            return float(big[len(big) // 2] + big[len(big) // 2 - 1])/ 2.0


