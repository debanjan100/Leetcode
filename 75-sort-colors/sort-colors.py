class Solution:
    def sortColors(self, nums: list[int]) -> None:
        
        low = 0                 # Next available position for 0
        mid = 0                 # Current element being examined
        high = len(nums) - 1    # Next available position for 2

        # Keep checking elements until mid crosses high
        while mid <= high:
            if nums[mid] == 0:
                # Move 0 to the front (low) and advance both pointers
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 belongs in the middle; just move to the next element
                mid += 1
            else:  # nums[mid] == 2
                # Move 2 to the end (high) and shrink the right boundary
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                # Note: Do NOT increase 'mid' because the swapped value
                # coming from 'high' hasn't been checked yet.
