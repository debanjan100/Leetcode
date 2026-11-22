from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        # Automatically defaults missing keys to 0
        seen_sums = defaultdict(int)
        seen_sums[0] = 1 
        
        for num in nums:
            current_sum += num
            # Check how many times (current_sum - k) has occurred so far
            count += seen_sums[current_sum - k]
            # Record the current running sum
            seen_sums[current_sum] += 1
            
        return count
