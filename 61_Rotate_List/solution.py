# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Compute length; find tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Reduce k to avoid unnecessary full rotations
        k = k % length
        if k == 0:
            return head
        
        # Keeps the list circular
        tail.next = head
        
        # Find new tail, using length k steps from beginning
        tail_new = head
        for _ in range(length - k - 1):
            tail_new = tail_new.next
        
        # And then new head is next of new tail
        new_head = tail_new.next
        tail_new.next = None  # Break cycle
        
        return new_head
