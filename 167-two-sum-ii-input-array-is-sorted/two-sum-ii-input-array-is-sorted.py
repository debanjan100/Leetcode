class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        prevMap = {}
        for i, n in enumerate(numbers):    
            diff = target - n      
            # If the difference is in our map, we found the pair
            if diff in prevMap:     
                return [prevMap[diff]+1, i+1]
            # Otherwise, store the current number and index
            prevMap[n] = i
