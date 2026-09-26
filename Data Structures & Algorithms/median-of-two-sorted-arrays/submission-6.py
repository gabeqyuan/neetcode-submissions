class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(a) + len(b)
        half = total // 2

        if len(a) > len(b):
            a, b = b, a
        l, r = 0, len(a) - 1
        while True:
            i = (l + r) // 2 #A partition
            j = half - i - 2 #B partition
            
            Aleft = a[i] if i >= 0 else float("-infinity")
            Aright = a[i + 1] if i + 1 < len(a) else float("infinity")
            Bleft = b[j] if j >= 0 else float("-infinity")
            Bright = b[j + 1] if (j + 1) < len(b) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (min(Aright, Bright) + max(Aleft, Bleft)) / 2
            elif Aleft > Bright:
                r = i - 1
            else: #Bleft > Aright
                l = i + 1
                