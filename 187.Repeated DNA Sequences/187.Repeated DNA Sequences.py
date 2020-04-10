# LeetCode Solution
# Zeyu Liu
# 2019.3.21
# 187.Repeated DNA Sequences

from typing import List
# method 1 stack，栈检验,这里需要注意的是两个都须使用set()，否则会超时(add比append更快)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        stack = set()
        opt = set()
        for i in range(len(s)-9):
            if s[i:i+10] not in stack:
                stack.add(s[i:i+10])
            else:
                opt.add(s[i:i+10])
        return list(opt)
# transfer method
solve = Solution()
print(solve.findRepeatedDnaSequences("AAAAAAAAAAAA"))

# method 2 方法1小优化，换成字典，最快
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        stack = dict()
        opt = set()
        for i in range(len(s)-9):
            a = s[i:i+10]
            if a not in stack:
                stack[a] = i
            else:
                opt.add(a)
        return list(opt)
# transfer method
solve = Solution()
print(solve.findRepeatedDnaSequences("AAAAAAAAAAAA"))
