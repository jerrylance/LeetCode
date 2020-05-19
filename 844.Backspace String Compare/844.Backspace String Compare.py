# LeetCode Solution
# Zeyu Liu
# 2019.4.15
# 53.Maximum Subarray

from typing import List
# method 1 stack
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1 = []
        stack2 = []
        for i in S:
        	if i == '#':
        		if stack1 != []:
        			stack1.pop()
        	else:
        		stack1.append(i)
        for i in T:
        	if i == '#':
        		if stack2 != []:
        			stack2.pop()
        	else:
        		stack2.append(i)
        return stack1 == stack2
# transfer method
solve = Solution()
print(solve.backspaceCompare("ab##", "c#d#"))

# method 2 O(1)space backward, 快，计数就可以了，需要进一步理解。
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        backS = backT = 0
        while True:
            while i >= 0 and (backS or S[i] == '#'):
                backS += 1 if S[i] == '#' else -1
                i -= 1
            while j >= 0 and (backT or T[j] == '#'):
                backT += 1 if T[j] == '#' else -1
                j -= 1
            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                return i == j == -1
            i, j = i - 1, j - 1
# transfer method
solve = Solution()
print(solve.backspaceCompare("ab##", "c#d#"))