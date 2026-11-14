class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        best = inf
        for i in range(len(nums)):
            s = 0
            for j in range(i, min(i + r, len(nums))): 
                s += nums[j]
                if j - i + 1 >= l and 0 < s < best:
                    best = s
        return -1 if best == inf else best