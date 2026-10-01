class Solution:
    def countAsterisks(self, s: str) -> int:
        count=0
        pip_count=0

        for i in range(len(s)):
            if s[i] =='*' and pip_count%2==0:
                count+=1
            if s[i] =='|':
                pip_count+=1
        return count

        