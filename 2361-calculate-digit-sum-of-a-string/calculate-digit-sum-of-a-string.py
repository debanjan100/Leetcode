class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            res = []
            for j in range(0,len(s), k):
                res.append(str(sum(int(c)for c in s[j: j+k])))
            s= "".join(res)
        return s