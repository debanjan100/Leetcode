class Solution:
    def minOperations(self, a: List[int], x: int, k: int) -> int:
        o,s=[0],SortedList([0]*x)
        f=lambda v,*_: max(s[x//2]-v,v-s[~x//2])
        for w,v in zip([0]*x+a,a):
            o.append(o[-1]-f(w)+f(v,s.remove(w),s.add(v)))
        return min(reduce(lambda d,j:accumulate(map(add,d,o[-~j*x:]),min),range(k),repeat(0)))