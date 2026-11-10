from functools import cache

class Solution:
    @cache  # <-- Put the cache right on top of the main function!
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n <= 1:
            return 1
            
        # Recursive step calling itself directly
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
