class Solution {
    public int rob(int[] nums) {
        int prev2 = 0; // Maximum money up to i-2
        int prev1 = 0; // Maximum money up to i-1

        for (int money : nums) {
            int current = Math.max(prev1, prev2 + money);
            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }
}