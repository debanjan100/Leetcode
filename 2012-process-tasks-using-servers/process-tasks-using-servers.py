class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapify(free)

        ans, busy = [], []  # busy: (second it frees up, weight, index)
        for s, t in enumerate(tasks):
            while busy and busy[0][0] <= s:  # done by second s
                heappush(free, heappop(busy)[1:])
            start, w, i = (s, *heappop(free)) if free else heappop(busy)  # none free: the first to finish takes it
            heappush(busy, (start + t, w, i))
            ans.append(i)

        return ans