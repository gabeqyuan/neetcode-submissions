class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = 1
        suff = 1
        result = [1] * len(nums)

        for i in range(len(nums)):
            result[i] = pref
            pref *= nums[i]
        
        for k in range(len(nums) - 1, -1, -1):
            result[k] *= suff
            suff *= nums[k]
        
        return result
        