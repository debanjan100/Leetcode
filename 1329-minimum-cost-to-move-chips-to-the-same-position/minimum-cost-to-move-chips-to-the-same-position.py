class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        evenCount = 0
        oddCount = 0

        for pos in position:
            if pos % 2==0:
                evenCount += 1
            else:
                oddCount += 1
        return min(oddCount, evenCount)