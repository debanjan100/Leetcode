class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i-1] == nums[i]:
                return nums[i]
        