class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []  # Stores indices of elements waiting for a next greater element
        
        # Traverse the array twice to simulate circular behavior
        for i in range(2 * n):
            curr_idx = i % n
            curr_val = nums[curr_idx]
            
            # While stack is not empty and current value is greater than the element at stack's top index
            while stack and nums[stack[-1]] < curr_val:
                prev_idx = stack.pop()
                res[prev_idx] = curr_val
            
            # Only push indices during the first pass
            if i < n:
                stack.append(curr_idx)
                
        return res
