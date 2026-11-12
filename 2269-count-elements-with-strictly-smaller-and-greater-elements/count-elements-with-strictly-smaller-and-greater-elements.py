class Solution:
    def countElements(self, nums: list[int]) -> int:
        res=0
        for val in nums:
            if val<max(nums) and val>min(nums):
                res+=1
        return res
        