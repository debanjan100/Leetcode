class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n > 1:
            matches += n // 2
            n = (n + 1) // 2
        return matches