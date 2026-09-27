class Solution:
    def minOperations(self, nums, k):
        return sum(nums) % k
        