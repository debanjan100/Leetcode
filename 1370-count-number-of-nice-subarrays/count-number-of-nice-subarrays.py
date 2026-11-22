class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k - 1)
    
    def atMost(self, nums: List[int], k: int) -> int:
        s, ans = 0, 0
        j = 0
        for i in range(len(nums)):
            s += nums[i] % 2
            while s > k:
                s -= nums[j] % 2
                j += 1
            ans += (i - j + 1)
        return ans