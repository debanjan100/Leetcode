class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        s,soc = source
        t, toc = target
        if s==t and soc == toc :
            return 0

        if s==t or soc==toc or abs(s-t)== abs(soc-toc):
            return 1
        return 2