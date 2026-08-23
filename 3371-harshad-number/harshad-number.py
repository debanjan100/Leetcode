class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum= 0
        Num = x
        while x != 0:
            digit = x % 10
            sum  = sum + digit
            x  = x // 10
        if Num % sum == 0:
            return sum
        else:
            return -1
        