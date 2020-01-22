# LeetCode Solution
# Zeyu Liu
# 2019.1.22
# 7.Reverse Integer

from typing import List
# method 1 利用字符串反转性质写法，速度一般，占用内存较小
class Solution:
    def reverse(self, x: int) -> int:
    	l1=[]
    	if x < -2**31 or x > 2**31 - 1:
        	return(0)
    	elif x > 0:
        	x = str(x)
        	for i,num in enumerate(x):
        		l1.append(x[-i-1])
        	x = int(''.join(l1))
        	if x < 2**31 - 1:
        		return(x)
        	else:
        		return(0)
    	elif x < 0:
        	x = str(abs(x))
        	for i,num in enumerate(x):
        		l1.append(x[-i-1])
        	x = int('-' + ''.join(l1))
        	if x > -2**31:
        		return(x)
        	else:
        		return(0)
    	else:
        	return(0)

# transfer method 
solve = Solution()
print(solve.reverse(1555534269))

# method 2 经典解法,最快
class Solution:
    def reverse(self, x: int) -> int:
        R = 0   
        flag = 1 
        if x < 0:
            x = abs(x)
            flag = -1 
        while x != 0:
            R = R * 10 + x % 10
            x = x // 10
        if -2147483647 < R < 2147483648:
            return R * flag
        else:
            return (0)
# transfer method
solve = Solution()
print(solve.reverse(-153))

# method 3 其他人写的更简洁的代码，和我的 method 1实质上是一样的
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            strg = str(x)
            if x >= 0 :
                revst = strg[::-1]
            else:
                temp = strg[1:] 
                temp2 = temp[::-1] 
                revst = "-" + temp2
            if int(revst) >= 2**31-1 or int(revst) <= -2**31: return 0
            else: return int(revst)
# transfer method
solve = Solution()
print(solve.reverse(-1536460))

# method 4 进一步简化代码后, 利用python切片，速度更快
class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x))          
        reversed = int(s[::-1]) #反排序        
        if reversed > 2**31-1:
            return 0

        return reversed if x > 0 else (reversed * -1)
# transfer method
solve = Solution()
print(solve.reverse(153429))

