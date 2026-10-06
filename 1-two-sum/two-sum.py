class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {} # val : index
        
        for i, n in enumerate(nums):
            diff = target - n
            # If the difference is in our map, we found the pair
            if diff in prevMap:
                return [prevMap[diff], i]
            # Otherwise, store the current number and index
            prevMap[n] = i