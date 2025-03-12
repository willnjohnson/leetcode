# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Interweave original and copied nodes
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
        
        # Set random pointers for copied nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next 
            curr = curr.next.next
        
        # Separate interweaved list into original and copied lists
        curr = head
        copied_head = head.next
        while curr:
            copied_node = curr.next
            curr.next = copied_node.next
            if copied_node.next:
                copied_node.next = copied_node.next.next
            curr = curr.next

        return copied_head
