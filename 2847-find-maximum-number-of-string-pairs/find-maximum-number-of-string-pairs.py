class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        seen = set()
        
        for word in words:
            # Check if the reversed word has been seen
            if word[::-1] in seen:
                count += 1
            else:
                # Otherwise, add the current word to the set
                seen.add(word)
                
        return count