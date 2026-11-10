class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        first, second = 2, 3
        for i in range(4, n + 1):
            third = first + second
            first = second
            second = third
        return second
