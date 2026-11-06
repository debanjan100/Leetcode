class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Initialize an empty list to store the resulting triplets
        result = []
        # Sort the input array. This is crucial for the two-pointer approach
        # and for efficiently skipping duplicate elements.
        nums.sort()
        
        n = len(nums)
        # Iterate through the array with 'i' as the first element of the triplet.
        # We only need to iterate up to n-2 because we need at least two more
        # elements (left and right) after 'i'.
        for i in range(n - 2):
            # Skip duplicate values for 'nums[i]'.
            # If the current element is the same as the previous one,
            # it means we've already considered all triplets with this value
            # as the first element in the previous iteration.
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Initialize two pointers: 'left' and 'right'.
            # 'left' starts just after 'i', and 'right' starts at the end of the array.
            left = i + 1
            right = n - 1
            
            # While the left pointer is less than the right pointer,
            # meaning there are still elements to consider for the pair.
            while left < right:
                # Calculate the current sum of the three elements.
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If the sum is zero, we found a valid triplet.
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for 'nums[left]'.
                    # Increment 'left' until it points to a different value
                    # to avoid adding duplicate triplets.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for 'nums[right]'.
                    # Decrement 'right' until it points to a different value
                    # to avoid adding duplicate triplets.
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers to continue searching for other unique triplets.
                    left += 1
                    right -= 1
                # If the sum is less than zero, we need a larger sum.
                # Increment 'left' to consider a larger second element.
                elif current_sum < 0:
                    left += 1
                # If the sum is greater than zero, we need a smaller sum.
                # Decrement 'right' to consider a smaller third element.
                else: # current_sum > 0
                    right -= 1
        
        # Return the list of unique triplets that sum to zero.
        return result