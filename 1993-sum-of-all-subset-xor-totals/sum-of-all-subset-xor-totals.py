class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def backtrack(index, xor):
            if index == len(nums):
                return xor

            # excluse
            notIncludeSum = backtrack(index + 1, xor)

            # include
            includeSum = backtrack(index + 1, xor ^ nums[index])

            return notIncludeSum + includeSum

        return backtrack(0, 0)