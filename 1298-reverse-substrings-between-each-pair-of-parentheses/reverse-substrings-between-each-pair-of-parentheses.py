class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = []
        result = []
        for i in range(len(s)):
            ch = s[i]
            if ch == '(':
                stack.append(len(result))
            elif ch == ')':
                start = stack.pop()
                result[start:] = result[start:][::-1]

            else:
                result.append(ch)

        return "".join(result)