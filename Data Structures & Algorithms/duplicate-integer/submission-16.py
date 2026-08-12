class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()

        for i, n in enumerate(nums):
            if n in hashmap:
                return True
            else:
                hashmap.add(n)
        return False