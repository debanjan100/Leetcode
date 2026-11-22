class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # Default answer if target is not found
        first = -1
        last = -1

        # 1. Binary search for the FIRST occurrence
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first = mid        # Save the index
                right = mid - 1    # Keep looking on the left side for an earlier match
            elif nums[mid] < target:
                left = mid + 1     # Target is in the right half
            else:
                right = mid - 1    # Target is in the left half

        # 2. Binary search for the LAST occurrence
        left, right = 0, len(nums) - 1  # Reset pointers
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last = mid         # Save the index
                left = mid + 1     # Keep looking on the right side for a later match
            elif nums[mid] < target:
                left = mid + 1     # Target is in the right half
            else:
                right = mid - 1    # Target is in the left half

        return [first, last]
