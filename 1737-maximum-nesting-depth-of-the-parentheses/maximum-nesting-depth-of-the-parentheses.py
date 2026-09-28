class Solution:
    def maxDepth(self, s: str) -> int:
        ans = depth = 0
        for ch in s:
            depth += (ch == "(") - (ch == ")")
            ans = max(ans, depth)
        return ans