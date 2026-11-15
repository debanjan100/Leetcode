class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = []
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                res.append(chars[0])
            else:
                break
        return "".join(res)
