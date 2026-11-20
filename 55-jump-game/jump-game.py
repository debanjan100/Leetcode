class Solution:

  def canJump(self, nums: List[int]) -> bool:
    max_reach = 0  # The farthest index we can reach so far

    for i in range(len(nums)):
      # If the current stone is beyond our farthest reach, we are stuck!
      if i > max_reach:
        return False

      # Update our farthest reach from this new stone
      max_reach = max(max_reach, i + nums[i])

    return True
