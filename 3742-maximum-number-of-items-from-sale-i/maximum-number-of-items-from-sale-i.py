class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        factors, prices = zip(*items)
        cheapest = min(prices)
        best = [money // cheapest for money in range(budget + 1)]  # no first copies yet: everything goes to the cheapest item
        for factor, price in items:
            gain = sum(other % factor == 0 for other in factors)  # the copy itself + a free copy of every other multiple
            for money in range(budget, price - 1, -1):  # backwards: one first copy per item
                best[money] = max(best[money], best[money - price] + gain)
        return best[budget]