class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        return [i for i in range(len(nums)) if nums[i]==target]