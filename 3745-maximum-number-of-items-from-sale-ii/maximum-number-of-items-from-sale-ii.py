class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        factors, prices = zip(*items)
        have = [0] * (len(items) + 1)  
        for factor in factors:
            have[factor] += 1
        deals = cache(lambda factor: sum(have[factor::factor]) - 1) 

        cheapest = min(prices)
        heap = [(price, factor) for factor, price in items if price < 2 * cheapest]
        heapify(heap)
        copies = 0
        while heap and heap[0][0] <= budget: 
            price, factor = heappop(heap)
            pairs = min(deals(factor), budget // price)
            copies += 2 * pairs
            budget -= pairs * price
        return copies + budget // cheapest