# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # We can use Floyd’s Tortoise and Hare algorithm for cycle detection
        # using a slow (tortoise) pointer and fast (hare) pointer
        tortoise = head
        hare = head
        
        # Traverse the list
        while hare and hare.next:
            tortoise = tortoise.next       # Tortoise moves one step
            hare = hare.next.next          # Hare moves two steps
            
            if tortoise == hare:           # Cycle detected if both pointers meet
                return True
        
        # Reached the end, no cycle
        return False
