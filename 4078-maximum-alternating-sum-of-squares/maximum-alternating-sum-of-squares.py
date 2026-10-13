class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Step 1 + 2: square every number, then sort (smallest on the left)
        a = sorted(x * x for x in nums)

        k = len(nums) // 2   # number of minus places

        # Step 3 + 4: add the big squares, subtract the k smallest ones
        return sum(a[k:]) - sum(a[:k])