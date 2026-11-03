class Solution:
    def minMoves(self, nums):
        return max(nums) * len(nums) - sum(nums)