class Solution:
    def waviness(self, x: int) -> int:
        s = str(x)

        cnt = 0

        for i in range(1, len(s) - 1):
            if ((s[i] > s[i - 1] and s[i] > s[i + 1]) or
                (s[i] < s[i - 1] and s[i] < s[i + 1])):
                cnt += 1

        return cnt

    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0

        for x in range(num1, num2 + 1):
            ans += self.waviness(x)

        return ans