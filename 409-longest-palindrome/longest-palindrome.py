class Solution:
    def longestPalindrome(self, s: str) -> int: 
        pal = set()
        for letter in s:
            if letter not in pal:
                pal.add(letter)
            else:
                pal.discard(letter)

        if len(pal) != 0:
            return len(s) - len(pal) +1
        return len(s)

        

        