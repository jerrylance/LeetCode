# LeetCode Solution
# Zeyu Liu
# 2019.1.20
# 2.Add Two Numbers

from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# method 1 利用ListNode概念
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode(0) #设置头节点值 head.val = 0，head.next = None
        ans=head # 初始化ans链表，ans链表指向head的0值地址
        jinwei=0
        while l1 and l2: #l1,l2都不为空
            x=l1.val
            y=l2.val
            s=x+y+jinwei #求和
            ans.next=ListNode(s%10) #将余数也就是两个数的和，赋值给下一个节点，ans.val = 0, ans.next = ListNode(s%10)
            jinwei=s//10 # 如果有进位+1
            ans=ans.next # ans.val = ListNode(s%10), ans.next = None,注意此时链表地址增加了1
            l1=l1.next # 求l1下一位数
            l2=l2.next # 求l2下一位数
        while l1: 
            x=l1.val
            s=(x+jinwei)
            ans.next=ListNode(s%10)
            jinwei=s//10
            ans=ans.next
            l1=l1.next
        while l2:
            x=l2.val
            s=(x+jinwei)
            ans.next=ListNode(s%10)
            jinwei=s//10
            ans=ans.next
            l2=l2.next
        if jinwei!=0: #如果有进位
            ans.next=ListNode(jinwei) # ans.val = ListNode(s%10), ans.next = jinwei

        return head.next #这里一定注意链表地址的概念！！！！切记，不可以用ans.next。
'''
关于链表的解释
节点：每个节点有两个部分，左边部分称为值域，用来存放用户数据；右边部分称为指针域，用来存放指向下一个元素的指针。python没指针，但是每个变量都可以指向下一个变量。
head:head节点永远指向第一个节点
tail: tail永远指向最后一个节点
None:链表中最后一个节点的指针域为None值
'''

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

node = Solution().addTwoNumbers(stringToListNode([2,3]),stringToListNode([5,7,4]))
out = listNodeToString(node)
print(out)


# method 2 步骤优化算法，原理method 1 一样
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val = l1.val + l2.val
        carrier, out = divmod(l1.val+l2.val, 10)# divmod 函数，输出//和%
        result = ListNode(out)
        temp = result
        
        l1=l1.next
        l2=l2.next
        while l1 or l2 or carrier:
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carrier, out = divmod(val1+val2+carrier, 10)
            
            temp.next = ListNode(out)
            temp = temp.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        return result
# transfer method       
node = Solution().addTwoNumbers(stringToListNode([5,3]),stringToListNode([5,7,1]))
out = listNodeToString(node)
print(out)