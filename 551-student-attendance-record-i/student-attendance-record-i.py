class Solution:
    def checkRecord(self, s: str) -> bool:
        late_count = 0
        absent_count = 0

        for i in range(len(s)):
            char = s[i]
            if char == 'A':
                absent_count += 1
                if absent_count >= 2:
                    return False
            if char == 'L':
                late_count += 1
                if late_count == 3:
                    return False
            else:
                late_count = 0
        
        return absent_count < 2 and late_count < 3