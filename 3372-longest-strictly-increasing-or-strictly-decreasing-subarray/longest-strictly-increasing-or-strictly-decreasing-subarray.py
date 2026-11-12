class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increase = 1
        decrease = 1
        res = 1
        for a, b in pairwise(nums):
            increase = increase + 1 if a>b else 1
            decrease = decrease + 1 if a<b else 1
            res = max(increase , decrease , res)
        return res