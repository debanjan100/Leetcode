class Solution:
    def checkString(self, s: str) -> bool:
        s = deque(s)
        while s and s[0] == "a":
            s.popleft()
        while s and s[0] == "b":
            s.popleft()
        return not s