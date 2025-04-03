# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode(0)
        large = ListNode(0)
        
        s, l = small, large
        
        while head:
            if head.val < x:
                s.next = head
                s = head
            else:
                l.next = head
                l = head
            head = head.next
        
        l.next = None
        s.next = large.next
        
        return small.next
