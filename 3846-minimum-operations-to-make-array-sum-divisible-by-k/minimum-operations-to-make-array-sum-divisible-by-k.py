class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total=0
        
        for i in range (len(nums)):
           total += nums[i]

        return total % k

        