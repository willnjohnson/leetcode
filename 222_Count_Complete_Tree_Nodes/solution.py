# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Compute left and right heights
        l, r = self.getHeight(root.left), self.getHeight(root.right)

        if l == r:
            return (1 << l) + self.countNodes(root.right) # Left subtree perfect
        
        # Right subtree perfect, but one level short
        return (1 << r) + self.countNodes(root.left)


    def getHeight(self, node: Optional[TreeNode]) -> int:
        # Calculate height of tree by traversing leftmost node
        # (i.e. all nodes in the last level are as far left as possible)
        height = 0
        while node:
            height += 1
            node = node.left
        return height