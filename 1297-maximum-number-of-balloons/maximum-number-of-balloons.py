class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Track counts of the specific letters we care about
        counts = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        
        # Loop through each character just like your original logic
        for ch in text:
            if ch in counts:
                counts[ch] += 1
        
        # 'l' and 'o' are needed twice per "balloon", so divide their counts by 2
        counts["l"] //= 2
        counts["o"] //= 2
        
        # The letter with the lowest count limits how many full words we can make
        return min(counts.values())
