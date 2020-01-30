# LeetCode Solution
# Zeyu Liu
# 2019.1.29
# 100.Same Tree

# Definition for a binary tree node.
# 这个编译有些问题，一些123，125应该返回false，结果却返回了true，但是在leetcode中运行没问题
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

# method 1 速度快，树的方法self.isSameTree()要牢记
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    	if p and q:
    		return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    	return p == q

# transfer method
solve = Solution()
print(solve.isSameTree(stringToTreeNode('123'),stringToTreeNode('12')))

# method 2 方法1的容易理解的解释
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
# transfer method
solve = Solution()
print(solve.isSameTree(stringToTreeNode('121'),stringToTreeNode('112')))


# method 3 方法1,2的优化,速度最快
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# transfer method
solve = Solution()
print(solve.isSameTree(stringToTreeNode('123'),stringToTreeNode('123')))