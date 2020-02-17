# LeetCode Solution
# Zeyu Liu
# 2019.2.15
# 83.Remove Duplicates from Sorted List

from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# method 1 head 和 temp关系，可以理解为temp是一个不断变化的指针，head是值。具体参考python赋值概念。
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
    	temp = head
    	while temp and temp.next:
    		if temp.val == temp.next.val:
    			temp.next = temp.next.next
    		else:
    			temp = temp.next
    	return head

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

node = Solution().deleteDuplicates(stringToListNode([1,1,2,3,3]))
out = listNodeToString(node)
print(out)
