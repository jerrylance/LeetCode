# LeetCode Solution
# Zeyu Liu
# 2019.6.12
# 824.Goat Latin

from typing import List
# method 1 straight forward
class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        res = []
        S = S.split()
        for i,v in enumerate(S):
        	if v[0] in vowel:
        		v += 'ma'
        	else:
        		v = v[1:] + v[0]
        		v += 'ma'
        	v += 'a' * (i + 1)
        	res.append(v)
        return " ".join(res)
# transfer method
solve = Solution()
print(solve.toGoatLatin("I speak Goat Latin"))

# method 2 one-line
class Solution:
    def toGoatLatin(self, S: str) -> str:
        return ' '.join((w if w[0].lower() in 'aeiou' else w[1:] + w[0]) + 'ma' + 'a' * (i + 1) for i, w in enumerate(S.split()))
# transfer method
solve = Solution()
print(solve.toGoatLatin("I speak Goat Latin"))