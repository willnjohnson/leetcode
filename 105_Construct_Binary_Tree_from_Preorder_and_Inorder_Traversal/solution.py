# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.i = 0
        self.inorder_map = {val: i for i, val in enumerate(inorder)}
        return self.build(preorder, 0, len(inorder) - 1)

    def build(self, preorder: List[int], left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None

        root_val = preorder[self.i]
        self.i += 1

        root = TreeNode(root_val)
        idx = self.inorder_map[root_val]

        root.left = self.build(preorder, left, idx - 1)
        root.right = self.build(preorder, idx + 1, right)

        return root