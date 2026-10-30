class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count=0
        n= len(words) # i can use this to get the range...
        for i in range(len(words)):
            for j in range(i+1,n):

                if words[i]== (words[j][::-1]) :
                    count+=1
        return count

        