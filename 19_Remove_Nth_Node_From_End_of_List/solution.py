# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        # Two pointers (slow and fast) initiated at dummy
        slow = fast = dummy
        
        # (1) Move fast pointer ahead by n steps
        for _ in range(n):
            fast = fast.next
        
        # (2) Move both fast and slow until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # (3) Remove the nth node from the end
        slow.next = slow.next.next
        
        return dummy.next