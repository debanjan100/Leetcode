class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums) 
        curr_sum = 0
        for i in range(len(nums)):
            right_sum = total - curr_sum - nums[i]

            if curr_sum == right_sum:
                return i

            curr_sum += nums[i] 

        return -1
