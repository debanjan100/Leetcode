class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)
        i = 0
        
        # 1. Check for minimum length
        if n < 3:
            return False
            
        # 2. Walk up
        while i + 1 < n and arr[i] < arr[i+1]:
            i += 1
            
        # 3. Check if peak is at start or end
        if i == 0 or i == n - 1:
            return False
            
        # 4. Walk down
        while i + 1 < n and arr[i] > arr[i+1]:
            i += 1
            
        # 5. Check if we reached the end
        return i == n - 1