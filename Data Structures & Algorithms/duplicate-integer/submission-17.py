class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for i, n in enumerate(nums):
            if n in hashmap:
                return True
            else:
                hashmap[n] = 1
        return False