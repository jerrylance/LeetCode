# LeetCode Solution
# Zeyu Liu
# 2019.2.5
# 206.Reverse Linked List
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# method 1 每个节点反转迭代
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
    	prev = None
    	curr = head
    	while curr:
    		later = curr.next
    		curr.next = prev
    		prev = curr
    		curr = later
    	return prev

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

node = Solution().reverseList(stringToListNode([1,2,3,4,5]))
out = listNodeToString(node)
print(out)
'''
一种易懂的解释，方法1是对下面解释的优化
很经典的问题，首先设置pre,cur,lat三个指针
pre   cur  lat
null   1 -> 2 -> 3 -> 4 -> 5 -> null
12
接着cur.next = pre
pre   cur  lat
null <-1    2 -> 3 -> 4 -> 5 -> null
12
接着pre = cur，cur = lat，lat = lat.next
      pre  cur  lat
null <-1    2 -> 3 -> 4 -> 5 -> null
12
重复上述操作直到lat=None。
                     pre  cur  lat
null <-1 <- 2 <- 3 <- 4    5 -> null

'''

# method 2 递归，head None head，建立双向连接
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
    	if head == None or head.next == None:
    		return head
    	nod = self.reverseList(head.next)
    	head.next.next = head
    	head.next = None
    	return nod

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

node = Solution().reverseList(stringToListNode([1,2,3,4,5]))
out = listNodeToString(node)
print(out)
'''
reverseList(head)返回输入的链表反转后的head，那么如果reverseList(head.next)的话
head
  1->2<-3<-4<-5
              |
             node
1234
我们此时只需要head.next.next=head，也就是先建立一个双向连接
head
  1->2<-3<-4<-5
   <-         |
             node
1234
然后再head.next=None，返回node即可。
      head
  null<-1<-2<-3<-4<-5
                    |
                   node
'''