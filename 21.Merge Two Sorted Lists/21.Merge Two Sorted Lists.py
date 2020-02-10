# LeetCode Solution
# Zeyu Liu
# 2019.2.8
# 21.Merge Two Sorted Lists

from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# method 1 literatively,常规方法
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    	head = tail = ListNode(0)
    	while l1 and l2:
    		if l1.val <= l2.val:
    			tail.next = l1
    			l1 = l1.next
    		else:
    			tail.next = l2
    			l2 = l2.next
    		tail = tail.next
    	tail.next = l1 or l2 # if one of them is at the end(means None), then the other one will append to the result directly.
    	return head.next

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

node = Solution().mergeTwoLists(stringToListNode([1,2,4]),stringToListNode([1,3,4]))
out = listNodeToString(node)
print(out)

# method 2 recursively，较快
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    	if not l1 or not l2:
        	return l1 or l2
    	if l1.val < l2.val:
        	l1.next = self.mergeTwoLists(l1.next, l2)
        	return l1
    	else:
        	l2.next = self.mergeTwoLists(l1, l2.next)
        	return l2

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

node = Solution().mergeTwoLists(stringToListNode([1,2,4]),stringToListNode([1,3,4]))
out = listNodeToString(node)
print(out)
