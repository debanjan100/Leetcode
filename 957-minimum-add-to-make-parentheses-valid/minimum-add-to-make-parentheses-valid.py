class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        [s:=s.replace('()','')for _ in s];return len(s)