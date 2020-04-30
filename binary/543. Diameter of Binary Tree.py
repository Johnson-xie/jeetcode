# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dia = 0

        def help(root):
            # back
            if not root:
                return 0

            # drill
            left = help(root.left)
            right = help(root.right)

            # process
            self.dia = max(self.dia, left + right)

            # clear
            return max(left, right) + 1

        help(root)
        return self.dia
