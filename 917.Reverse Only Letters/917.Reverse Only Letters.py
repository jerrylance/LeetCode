# LeetCode Solution
# Zeyu Liu
# 2019.5.15
# 917.Reverse Only Letters

from typing import List
# method 1 straight forward
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        l = [0] * len(S)
        s1 = ''
        for i in range(len(S)):
        	if not S[i].isalpha():
        		l[i] = S[i]
        	else:
        		s1 += S[i]
        s1 = s1[::-1]
        j = 0
        for i in range(len(l)):
        	if l[i] == 0:
        		l[i] = s1[j]
        		j += 1
        return ''.join(l)
# transfer method
solve = Solution()
print(solve.reverseOnlyLetters("Test1ng-Leet=code-Q!"))

# method 2 two points
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        l, r = 0, len(S) - 1
        while l < r:
            if not S[l].isalpha():
                l += 1
            elif not S[r].isalpha():
                r -= 1
            else:
                S[l], S[r] = S[r], S[l]
                l += 1
                r -= 1
        return ''.join(S)
# transfer method
solve = Solution()
print(solve.reverseOnlyLetters("Test1ng-Leet=code-Q!"))