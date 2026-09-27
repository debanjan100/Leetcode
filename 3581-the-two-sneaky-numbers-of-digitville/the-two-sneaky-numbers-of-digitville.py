class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
     n = len(nums) 
     res= []
     for i in range(n):
        for j in range(i+1, n):
           if nums[i] == nums[j]:
               res.append(nums[i])
     return res  # Outside all loops! 