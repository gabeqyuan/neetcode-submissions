class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        result = []
        for key, value in enumerate(nums):
            diff = target - nums[key]
            if target - nums[key] in seen:
                result += [seen[diff], key]
            seen[value] = key
        return result

                
    


