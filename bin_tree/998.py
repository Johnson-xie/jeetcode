# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        self.dummy = head
        return self.help(head, root)

    def help(self, head, root)
        if not head:
            return True
        if not root:
            return False
        if root.val == head.val:
            return self.help(head.next, root.left) or self.help(head.next, root.right)

        return self.help(self.dummy, root.left) or self.help(self.dummy, root.right)