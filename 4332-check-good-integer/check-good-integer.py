class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digit_sum = 0
        square_sum = 0
        while(n > 0):
            rem = n % 10
            digit_sum += rem
            square_sum = square_sum + rem**2
            n //= 10
        return square_sum - digit_sum >= 50