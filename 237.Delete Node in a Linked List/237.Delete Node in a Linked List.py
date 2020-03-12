# LeetCode Solution
# Zeyu Liu
# 2019.3.3
# 237.Delete Node in a Linked List

from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# method 1 把指定Node的Value更改成下一个Node的值
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

# transfer method    
def stringToListNode(input):
    numbers = input # list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr
def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

node = Solution().deleteNode(stringToListNode([3,5,2]))
out = listNodeToString(node)
print(out)

# 其实不能真正意义上的删除指定的Node，因为没有给与Previous Node。
# 所以从根本意义上，只能取巧的解决这个问题。题目刻意给了很多附件的条件，比如链表value没有重复，并且指定Node不是Tail，其实都是在给正解做铺垫
# 我们真正删除的是指定Node的下一个Node，然后把指定Node的Value更改成下一个Node的值罢了。
# 为什么这个node.next.next在这里是没问题的，因为题目告诉了说指定的Node不为Tail，所以我们不用担心这个Edge Case。