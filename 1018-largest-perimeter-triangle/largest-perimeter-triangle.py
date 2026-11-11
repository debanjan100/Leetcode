class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1,1,-1):
            if nums[i-1]+nums[i-2] > nums[i]:
                return nums[i]+ nums[i-1]+ nums[i-2]

        return 0
        