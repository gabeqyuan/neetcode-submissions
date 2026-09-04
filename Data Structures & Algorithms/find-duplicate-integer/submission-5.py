class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        newSlow = 0
        while True:
            newSlow = nums[newSlow]
            slow = nums[slow]
            if newSlow == slow:
                break

        return newSlow