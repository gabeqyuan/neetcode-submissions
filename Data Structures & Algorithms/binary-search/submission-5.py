class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #nums = [-1,0,2,4,6,8], target = 4 target = 4
        #.            L M   R
        n = len (nums)
        left = 0 
        right = n - 1
        while left <= right:
            middle = right - left // 2
            if nums[middle] == target:
                return middle 
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
            print(middle)
        return -1