# LeetCode Solution
# Zeyu Liu
# 2019.3.16
# 412.Fizz Buzz

from typing import List
# method 1 列表操作,注意输出格式
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        s = [x+1 for x in range(n)]
        for i in range(len(s)):
        	if s[i] % 15 == 0:
        		s[i] = 'FizzBuzz'
        	elif s[i] % 3 == 0:
        		s[i] = 'Fizz'
        	elif s[i] % 5 == 0:
        		s[i] = 'Buzz'
        	else:
        		s[i] = str(s[i])
        return s
# transfer method
solve = Solution()
print(solve.fizzBuzz(15))

# method 2 方法1优化
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
    	s = []
    	i = 1
    	for i in range(1,n+1):
    		if i % 15 == 0:
    			s.append('FizzBuzz')
    		elif i % 3 == 0:
    			s.append('Fizz')
    		elif i % 5 == 0:
    			s.append('Buzz')
    		else:
    			s.append(str(i))
    	return s
# transfer method
solve = Solution()
print(solve.fizzBuzz(15))

# method 3 一行代码[x for x in range(n)]应用
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [str(i) * (i % 3 != 0 and i % 5 != 0) + "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) for i in range(1, n + 1)]
# transfer method
solve = Solution()
print(solve.fizzBuzz(15))