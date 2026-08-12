class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        L = 0
        R = n - 1
        minimum = nums[0]
        while L <= R:
            if nums[L] < nums[R]:
                minimum = min(minimum, nums[L])
                break
            mid = (R+L) // 2
            minimum = min(nums[mid], minimum)
            if nums[mid] < nums[R]:
                R = mid - 1
            else:
                L = mid + 1
        
        return minimum
         