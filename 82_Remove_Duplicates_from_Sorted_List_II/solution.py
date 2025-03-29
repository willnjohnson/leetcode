# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) 
        dummy.next = head
        prev = dummy

        while head:
            if head.next and head.val == head.next.val:
                # Skip nodes with same value
                while head.next and head.val == head.next.val:
                    head = head.next

                # Remove duplicates
                prev.next = head.next
            else:
                # Move prev forward (i.e. if no duplicates)
                prev = prev.next

            # Move head forward
            head = head.next

        return dummy.next