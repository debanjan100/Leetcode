class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:

        def dfs(i: int)-> None:

            ch = s[i]

            if ch in ancestor: prev = ancestor[ch]
            else: prev = None

            ancestor[ch] = i

            for node in graph[i]:
                dfs(node)
                ans[parent[node]]+= ans[node]

            ancestor[ch] = prev
            if prev is None: return
            parent[i] = prev

            return 


        ans = [1] * len(s)
        graph, ancestor = defaultdict(list), defaultdict(int)
        
        for node, par in enumerate(parent):
            graph[par].append(node)
        
        dfs(0)

        return ans