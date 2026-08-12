class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        index = -1 
        
        for i in range(n):
            if nums[i] == target:
                return i 
        return index