import math
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_val= nums[0]
        sum = 0
        for num in nums:
            min_val = min(min_val,num)
            sum +=num

        return sum-(len(nums)*min_val)