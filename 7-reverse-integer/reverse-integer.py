class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        ans = 0
        sign = 1 if x > 0 else -1
        x = abs(x)  # work with positive number
        
        while x != 0:
            rem = x % 10
            x //= 10
            
            # Check overflow BEFORE multiplying
            if ans > (INT_MAX // 10) or (ans == INT_MAX // 10 and rem > 7):
                return 0
            
            ans = ans * 10 + rem
        
        return sign * ans