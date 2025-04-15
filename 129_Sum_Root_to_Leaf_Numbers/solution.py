# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Initial traversal
        return self.dfs(root, 0)
    
    def dfs(self, node: Optional[TreeNode], num: int) -> int:
        # Base case
        if not node:
            return 0
        
        num = (num * 10) + node.val

        # Reached leaf
        if not node.left and not node.right:
            return num
        
        # Recursive case
        return self.dfs(node.left, num) + self.dfs(node.right, num)