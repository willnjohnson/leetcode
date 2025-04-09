# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Final step
        return self.check(root.left, root.right)

    def check(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        # Base case
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        
        # Recursion step
        return (t1.val == t2.val and
                self.check(t1.left, t2.right) and
                self.check(t1.right, t2.left))