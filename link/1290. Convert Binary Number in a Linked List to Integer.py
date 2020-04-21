# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        value = 0
        while head:
            # value = value * 2 + head.val
            # value = (value << 1) + head.val
            value = (value << 1) | head.val
            head = head.next

        return value

"""
100a+10b+c=((10∗a+b)∗10)∗10+c
"""
