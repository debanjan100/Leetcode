class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = {'a','e','i','o','u'}
        vow = [0] * 26
        const = [0] * 26
        
        for ch in s:
            idx = ord(ch) - ord('a')
            if ch in vowel:
                vow[idx] += 1
            else:
                const[idx] += 1
        
        return max(vow) + max(const)