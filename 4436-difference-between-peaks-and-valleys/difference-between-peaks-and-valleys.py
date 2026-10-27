class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        peak = 0
        valley = 0

        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                peak += nums[i]
            elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                valley += nums[i]

        return peak - valley