class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        count = {}

        for num in nums: 
            count[num] = count.get(num, 0) + 1
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # Fix 3: skip duplicate i
                continue
            count[nums[i]] -= 1

            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue 
                count[nums[j]] -= 1
                target = -(nums[i] + nums[j])
                if count.get(target, 0) > 0 and target >= nums[j]:
                    result.append([nums[i], nums[j],target])
                count[nums[j]] += 1
            count[nums[i]] += 1

        return result

