# LeetCode Solution
# Zeyu Liu
# 2019.2.9
# 8.String to Integer (atoi)

from typing import List
# method 1 字符串转化性质，小心浮点数float,判断条件，try，except的应用
class Solution:
    def myAtoi(self, str: str) -> int:
    	Int_min = -2147483648
    	Int_max = 2147483647
    	if str:
    		str1 = str.split(' ')
    		for i in str1:
    			if i != '':#这里不要用remove方法，因为会造成列表前后不同，如果想用，就新建一个一样的列表，只修改第二个列表
    				i = i
    				if i[0] == '+':
    					for m in range(1,len(i)+1):
    						try:
    							int(float(i[m]))
    						except:
    							break
    					try:
    						if int(float(i[0:m])) < Int_min:
    							return Int_min
    						elif int(float(i[0:m])) > Int_max:
    							return Int_max
    						else:
    							return int(float(i[0:m]))
    					except:
    						return 0
    				elif i[0] != '-':
    					for n in range(len(i)+1):
    						try:
    							int(float(i[n]))
    						except:
    							break
    					try:
    						if int(float(i[0:n])) < Int_min:
    							return Int_min
    						elif int(float(i[0:n])) > Int_max:
    							return Int_max
    						else:
    							return int(float(i[0:n]))
    					except:
    						return 0
    				elif i[0] == '-':
    					for m in range(1,len(i)+1):
    						try:
    							int(float(i[m]))
    						except:
    							break
    					try:
    						if int(float(i[0:m])) < Int_min:
    							return Int_min
    						elif int(float(i[0:m])) > Int_max:
    							return Int_max
    						else:
    							return int(float(i[0:m]))
    					except:
    						return 0
    	return 0
# transfer method    
solve = Solution()
print(solve.myAtoi("-3.234234234aff"))

# method 2 strip()去掉字符串之间的空格,isdigit()判断是否是数字
class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.strip()
        if not s: 
        	return 0        
        int_max, int_min = 2**31 - 1, -2**31
        sign, res, i, n = 1, 0, 0, len(s)
        if s[i] in ['+', '-']:
            if s[i] == '-':
            	sign = -1
            i += 1
        while i < n and s[i].isdigit():
            res = 10 * res + int(s[i])
            if res * sign > int_max: 
            	return int_max
            if res * sign < int_min: 
            	return int_min
            i += 1
        return res * sign
# transfer method    
solve = Solution()
print(solve.myAtoi("-3.234234234a"))