class Solution:
    def rob(self, nums: List[int]) -> int:
        #every house has decisions either rob and skip or not rob and rob the next one 
        # each item of the dp table should be the maximum at that time 
        dp = [0] * len(nums) 
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        # either rob +  i - 2  or take i - 1 and no rob] 
        # dp [2,1,3,2]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        return max(dp)
