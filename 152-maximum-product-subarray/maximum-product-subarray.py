class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # If the array is empty, there's no product, though constraints say nums.length >= 1.
        

        # Initialize max_so_far and min_so_far with the first element.
        # max_so_far tracks the maximum product ending at the current position.
        # min_so_far tracks the minimum product ending at the current position.
        # We need to track both because a negative number multiplied by another negative
        # number can yield a large positive number.
        max_so_far = nums[0]
        min_so_far = nums[0]

        # The overall result is initialized with the first element.
        # This will store the maximum product found across all subarrays.
        result = max_so_far

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            current_num = nums[i]

            # We need to store the previous max_so_far because min_so_far's
            # calculation also depends on the max product from the previous step.
            temp_max = max_so_far

            # Calculate the new max_so_far ending at the current position.
            # It can be either:
            # 1. The current number itself (starting a new subarray).
            # 2. The product of the current number and the previous max_so_far.
            # 3. The product of the current number and the previous min_so_far (important for negatives).
            max_so_far = max(current_num, current_num * temp_max, current_num * min_so_far)

            # Calculate the new min_so_far ending at the current position.
            # It can be either:
            # 1. The current number itself (starting a new subarray).
            # 2. The product of the current number and the previous max_so_far.
            # 3. The product of the current number and the previous min_so_far.
            min_so_far = min(current_num, current_num * temp_max, current_num * min_so_far)

            # Update the overall result with the maximum product found so far.
            result = max(result, max_so_far)

        return result