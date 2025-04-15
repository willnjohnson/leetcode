# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # DFS, but with weights (initialized at negative infinity)
        self.max_sum = float('-inf')

        # Initial traversal
        self.dfs(root)
        return self.max_sum

    def dfs(self, node: Optional[TreeNode]) -> int:
        # Base case
        if not node:
            return 0
        
        # Recursive case
        # Calculate each leaf for given level (left and right) recursively
        l = max(self.dfs(node.left), 0)
        r = max(self.dfs(node.right), 0)

        # Update maximum sum
        self.max_sum = max(self.max_sum, l + r + node.val)
        return max(l, r) + node.val