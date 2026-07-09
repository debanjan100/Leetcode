class Solution:
    def romanToInt(self, s: str) -> int:
        roma = {'I':1, 'V':5, 'X':10, 'L':50,
                 'C':100, 'D':500, 'M':1000}
        
        resul = 0
        for i in range(len(s)):
            curr = roma[s[i]]
            next_val = roma[s[i+1]] if i+1 < len(s) else 0
            
            if curr < next_val:
                resul-= curr
            else:
                resul += curr
        
        return resul