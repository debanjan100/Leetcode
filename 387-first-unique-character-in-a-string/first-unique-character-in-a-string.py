class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = {}

        for ch in s:
            mp[ch] = mp.get(ch, 0) + 1

        for i in range(len(s)):
            if mp[s[i]] == 1:
                return i

        return -1

