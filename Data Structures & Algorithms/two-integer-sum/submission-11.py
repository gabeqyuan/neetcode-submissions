class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        result = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if target - nums[i] in seen:
                result += [seen[diff], i]
            seen[nums[i]] = i
        return result

                
    


