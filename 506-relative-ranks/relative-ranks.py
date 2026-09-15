class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        maxHeap = []
        for i, s in enumerate(score):
            heappush(maxHeap, (-s, i))
        
        res = [0] * len(score)
        place = 1
        while maxHeap:
            pos = heappop(maxHeap)[1]
            if place > 3:
                rank = str(place)
            elif place == 1:
                rank = "Gold Medal"
            elif place == 2:
                rank = "Silver Medal"
            elif place == 3:
                rank = "Bronze Medal"
            
            res[pos] = rank
            place +=1
            
        return res