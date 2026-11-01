class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        mask = n
        for i in (1, 2, 4, 8, 16):
            mask |= mask >> i
        return ~n & mask