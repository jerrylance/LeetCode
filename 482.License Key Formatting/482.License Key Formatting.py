# LeetCode Solution
# Zeyu Liu
# 2019.4.23
# 482.License Key Formatting

from typing import List
# method 1 straightforward, ''.join(str.split())
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
    	S = ''.join(S.split('-')).upper()
    	first = len(S) % K
    	res = ''
    	count = -first
    	for i in range(len(S)):
    		if i == first and first != 0:
    			res += '-'
    		if count == K:
    			res += '-'
    			count = 0
    		res += S[i]
    		count += 1
    	return res
# transfer method
solve = Solution()
print(solve.licenseKeyFormatting("5F3Z-2e-9-w", 4))

# method 2 反序, replace()
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
    	S = ''.join(S.split('-')).upper()[::-1]
    	#S = S.replace("-", "").upper()[::-1]
    	return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]
# transfer method
solve = Solution()
print(solve.licenseKeyFormatting("5F3Z-2e-9-w", 4))