# LeetCode Solution
# Zeyu Liu
# 2019.4.11
# 38.Count and Say

from typing import List
# method 1 巧妙将字符串末尾加‘0’, 防止判定时系数溢出, 同时减少了判定条件，快
class Solution:
    def countAndSay(self, n: int) -> str:
    	s = '10'
    	s1 = ''
    	count = 0
    	for i in range(n-1):
    		for j in range(len(s)-1):
    			count += 1
    			if s[j] != s[j+1]:
    				s1 += str(count) + str(s[j])
    				count = 0
    		s = s1 + '0'
    		s1 = ''
    	return s[:-1]
# transfer method
solve = Solution()
print(solve.countAndSay(7))

# method 2 str()常规思路，通过设置s[0]的值，不会造成系数溢出
class Solution:
    def countAndSay(self, n: int) -> str:
        s='1'
        for i in range(n-1):
            num = s[0]
            count = 0
            s1 = ''
            for j in s:
                if j == num:
                    count += 1
                else:
                    s1 += str(count) + num
                    count = 1
                    num = j
            s1 += str(count) + num
            s = s1
        return s
# transfer method
solve = Solution()
print(solve.countAndSay(7))

# method 3 recursive, 原理同方法2
class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(n-1):
            res = self.helper(res)
        return res    
    def helper(self, n):
        count, i, res = 1, 0, ''
        while i < len(n) - 1:
            if n[i] == n[i+1]:
                count += 1
            else:
                res += str(count) + n[i]
                count = 1
            i += 1
        res += str(count) + n[i]
        return res
# transfer method
solve = Solution()
print(solve.countAndSay(7))

