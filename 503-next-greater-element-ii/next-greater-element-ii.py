class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [-1]*n
        for i in range(2*n-1,-1,-1):
            curr = nums[i%n]
            while stack and curr>=stack[-1]:
                stack.pop()
            if i < n:
                res[i] = stack[-1] if stack else -1
            stack.append(curr)
        return res