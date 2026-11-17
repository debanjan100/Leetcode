class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        divisors = [[] for _ in range(n + 1)]  # divisors[length]: every d < length that divides it
        for d in range(1, n):
            for length in range(2 * d, n + 1, d):
                divisors[length].append(d)

        @cache
        def peel(i: int, j: int, d: int) -> int:  # s[i:j] in blocks of d: the outer pair of blocks, then the inside
            if j - i <= d:
                return 0  # no blocks or a single block: nothing to pair
            return sum(map(ne, s[i:i + d], s[j - d:j])) + peel(i + d, j - d, d)

        @cache
        def cost(i: int, j: int) -> int:  # changes to make s[i:j] a semi-palindrome
            return min(peel(i, j, d) for d in divisors[j - i])

        best = {0: 0}  # best[j]: the fewest changes for s[:j] cut into the pieces placed so far
        for pieces in range(1, k):  # every piece but the last
            room = range(2 * pieces, n - 2 * (k - pieces) + 1)  # 2 letters for each piece, placed or still to come
            best = {j: min(best[i] + cost(i, j) for i in best if i <= j - 2) for j in room}
        return min(best[i] + cost(i, n) for i in best)  # the last piece ends at n