class Solution:
    def countElements(self, nums: list[int]) -> int:
        nums.sort()
        cnt = 0
        for i in range(1,len(nums)-1):
            if nums[i]>nums[0] and nums[i]<nums[-1]:
                cnt+=1
        return cnt
        