class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k != 0:
            # Overwrite the entire array by combining the last k elements 
            # with everything except the last k elements.
            nums[:] = nums[-k:] + nums[:-k]
