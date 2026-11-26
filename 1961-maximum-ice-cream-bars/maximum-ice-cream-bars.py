from typing import List


class Solution:

  def maxIceCream(self, costs: List[int], coins: int) -> int:
    n = len(costs)
    costs.sort()
    i = 0

    while i < n and coins >= costs[i]:
      coins -= costs[i]
      i += 1

    return i
