class Solution:
    def maxLength(self, nums: list[int]) -> int:
        best, left, product = 2, 0, 1
        for right, x in enumerate(nums):
            while gcd(product, x) > 1:
                product //= nums[left]
                left += 1
            product *= x
            best = max(best, right - left + 1)
        return best