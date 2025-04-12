# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                # Find rightmost node of left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right

                # Connect rightmost node's right with current's right subtree
                prev.right = curr.right

                # Move left subtree right
                curr.right = curr.left
                curr.left = None

            # Move right to next node
            curr = curr.right