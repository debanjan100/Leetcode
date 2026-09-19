class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        opened = 0
        
        for c in s:
            if c == '(':
                if opened > 0:
                    res.append(c)
                opened += 1
            else:
                opened -= 1
                if opened > 0:
                    res.append(c)
                    
        return "".join(res)