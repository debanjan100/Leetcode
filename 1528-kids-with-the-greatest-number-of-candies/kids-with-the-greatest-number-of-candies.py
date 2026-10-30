class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        result= []
        for candy in candies:
            result.append(candy + extraCandies >= max_candies)
        return result