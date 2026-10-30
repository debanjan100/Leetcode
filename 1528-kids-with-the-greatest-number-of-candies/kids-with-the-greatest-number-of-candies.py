class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        ans= []
        for candy in candies:
            ans.append(candy + extraCandies >= max_candies)
        return ans