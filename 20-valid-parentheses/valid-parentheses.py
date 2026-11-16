class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for ch in s:
            if ch in mapping.values():
                stack.append(ch)
            elif ch in mapping:
                if not stack or mapping[ch] != stack.pop():
                    return False
        return not stack
        