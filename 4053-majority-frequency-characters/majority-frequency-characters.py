class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        c = Counter(s)
        res = defaultdict(list)
        for i in c:
            res[c[i]].append(i)
        
        new = defaultdict(list)
        for i in res:
            new[len(res[i])].append(i)
        
        w = res[max(new[max(new)])]
        return ''.join(w)