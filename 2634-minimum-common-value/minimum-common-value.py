class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Cast the sorted arrays into double-ended queues
        queue1 = deque(nums1)
        queue2 = deque(nums2)
        
        # Erode the streams from the front until a match or exhaustion
        while queue1 and queue2:
            head1 = queue1[0]
            head2 = queue2[0]
            
            if head1 == head2:
                return head1  # First mutual element encountered is guaranteed the minimum
            elif head1 < head2:
                queue1.popleft()  # Erode the smaller value
            else:
                queue2.popleft()  # Erode the smaller value
                
        return -1