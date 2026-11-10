from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def helper(stairs: int) -> int:
            if stairs <= 1:
                return 1
            return helper(stairs - 1) + helper(stairs - 2)
            
        return helper(n)