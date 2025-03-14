# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt_node = 0
        tmp = head

        while tmp:
            cnt_node += 1
            tmp = tmp.next
        
        dummy = ListNode(0)
        dummy.next = head
        prev_end = dummy
        
        # Loop through the list, reversing k nodes at a time
        while cnt_node >= k:
            start = prev_end.next
            end = start
            for _ in range(k - 1):
                end = end.next
            
            # Save next k group's start
            next_start = end.next
            end.next = None
            
            # Reverse k group
            prev, curr = None, start
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            # Connect previous part of list to the reversed group
            # Then move prev_end to end of reversed group
            prev_end.next = prev
            start.next = next_start
            prev_end = start
            
            # Decrease remaining node count
            cnt_node -= k
        
        return dummy.next