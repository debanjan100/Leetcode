class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        def far(a):  # no b in [a - d, a + d]
            return all(abs(a - b) > d for b in arr2)

        return sum(map(far, arr1))