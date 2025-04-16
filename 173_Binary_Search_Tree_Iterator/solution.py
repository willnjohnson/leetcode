# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # Stack to maintain FIFO ordering
        self.stack = []

        # Append in-order from left-most root
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        # Pop from stack, setting current to right
        node = self.stack.pop()
        curr = node.right

        # Append current (right node), then set current (left node)
        while curr:
            self.stack.append(curr)
            curr = curr.left

        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()