class Solution(object):
    def isMonotonic(self, nums):
        # Handle edge cases first
        if len(nums) <= 2:
            return True
        
        # Track whether we see increasing or decreasing pairs
        increased = False
        decreased = False
        
        # Iterate through consecutive pairs
        for i in range(len(nums) - 1):
            # Check what happens when elements differ
            if nums[i] < nums[i + 1]:
                increased = True
            elif nums[i] > nums[i + 1]:
                decreased = True
            
            # What's the key condition here?
            if increased and decreased:
                return False
        
        return True