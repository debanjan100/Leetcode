class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        res = []
        nums.sort()
        for i, val in enumerate(nums): 
            if val == target:           
                res.append(i)         
        return res                      