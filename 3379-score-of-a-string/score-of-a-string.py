class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        a = len(s)-1
        for i in range (0,a):
            score += abs(ord(s[i]) - ord(s[i+1]))
        return score