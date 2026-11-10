class Solution:
    def __init__(self):
        # A dictionary to remember past answers: {n: result}
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        # 1. Base cases
        if n <= 1:
            return 1
            
        # 2. Check the memo: If we already calculated this 'n', just return it
        if n in self.memo:
            return self.memo[n]
            
        # 3. Calculate and save the result into our memo before returning
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]
