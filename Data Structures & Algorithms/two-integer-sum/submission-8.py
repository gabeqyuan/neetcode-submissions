class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # if you do target- the number 
        hashmap = {}
        for i, n in enumerate(nums):

            if target - nums[i] in hashmap:
                return [hashmap[target-n], i]

            hashmap[n] = i


