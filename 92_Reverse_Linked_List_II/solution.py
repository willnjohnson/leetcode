# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Step 1: Create a dummy node to handle edge cases where head might change
        dummy = ListNode(0)
        dummy.next, prev = head, dummy
        
        for _ in range(left - 1):
            prev = prev.next
        
        # Reverse sublist from left to right
        curr = prev.next
        next_node = None
        for _ in range(right - left + 1):
            tmp = curr.next
            curr.next = next_node
            next_node = curr
            curr = tmp
        
        # Connect back reversed sublist
        prev.next.next = curr
        prev.next = next_node
        
        return dummy.next