class Solution:
    def singleNumber(self, nums):
        ones, twos = 0, 0

        for num in nums:
            # Update ones and twos
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones 