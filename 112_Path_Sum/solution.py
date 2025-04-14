# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        # Base case (leaf node)
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recursive case (check left and right subtrees)
        # Use parent sum to add up with next leaf nodes
        t = targetSum - root.val

        return self.hasPathSum(root.left, t) or self.hasPathSum(root.right, t)