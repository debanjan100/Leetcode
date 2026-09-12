class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""

        for i in range(n):
            # Odd length palindrome
            st = end = i
            while st >= 0 and end < n and s[st] == s[end]:
                st -= 1
                end += 1
            temp = s[st+1:end]
            if len(temp) > len(res):
                res = temp

            # Even length palindrome
            st, end = i, i+1
            while st >= 0 and end < n and s[st] == s[end]:
                st -= 1
                end += 1
            temp = s[st+1:end]
            if len(temp) > len(res):
                res = temp

        return res