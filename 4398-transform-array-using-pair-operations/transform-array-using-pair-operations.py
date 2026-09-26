class Solution:
    def canTransform(self, source: list[int], target: list[int]) -> bool:
        if len(source)!= len(target):
            return False
        if len(source)==1:
            return source == target
        return sum(source) == sum(target)