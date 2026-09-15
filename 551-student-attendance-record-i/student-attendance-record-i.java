class Solution {
    public boolean checkRecord(String s) {
        int absences = 0;
        int consecutiveLate = 0;

        for (char ch : s.toCharArray()) {
            if (ch == 'A') {
                absences++;
                consecutiveLate = 0;
            } else if (ch == 'L') {
                consecutiveLate++;
            } else { // 'P'
                consecutiveLate = 0;
            }

            // More than 1 absence OR 3 consecutive late days
            if (absences >= 2 || consecutiveLate >= 3) {
                return false;
            }
        }

        return true;
    }
}
