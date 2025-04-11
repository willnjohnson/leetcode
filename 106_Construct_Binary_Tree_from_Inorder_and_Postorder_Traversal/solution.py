# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.i = len(postorder) - 1
        self.idx_map = {val: idx for idx, val in enumerate(inorder)}
        self.postorder = postorder
        return self.build(0, len(inorder) - 1)

    def build(self, in_left: int, in_right: int) -> Optional[TreeNode]:
        if in_left > in_right:
            return None

        root_val = self.postorder[self.i]
        root = TreeNode(root_val)

        index = self.idx_map[root_val]
        self.i -= 1

        root.right = self.build(index + 1, in_right)
        root.left = self.build(in_left, index - 1)

        return root