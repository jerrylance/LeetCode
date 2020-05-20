# LeetCode Solution
# Zeyu Liu
# 2019.4.16
# 942.DI String Match

from typing import List
# method 1 栈的思想，首尾分别取值，较慢
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        stack = [i for i in range(len(S)+1)]
        res = []
        for i in S:
          	if i == 'I':
          		res.append(stack.pop(0))
          	elif i == 'D':
          		res.append(stack.pop())
        res.append(stack.pop())
        return res
# transfer method
solve = Solution()
print(solve.diStringMatch("IDID"))

# method 2 思路和方法1类似，使用计数替代pop()，快
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        I = 0
        D = len(S)
        res = []
        for i in S:
          	if i == 'I':
          		res.append(I)
          		I += 1
          	elif i == 'D':
          		res.append(D)
          		D -= 1
        res.append(I)
        return res
# transfer method
solve = Solution()
print(solve.diStringMatch("IDID"))