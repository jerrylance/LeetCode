# LeetCode Solution
# Zeyu Liu
# 2019.3.7
# 500.Keyboard Row

from typing import List
# method 1 暴力法，循环迭代，较快
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
    	w1 = 'QqWwEeRrTtYyUuIiOoPp'
    	w2 = 'AaSsDdFfGgHhJjKkLl'
    	w3 = 'ZzXxCcVvBbNnMm'
    	w = []
    	for i in words:
    		c = 0
    		if i[0] in w1:
    			for j in i:
    				if j not in w1:
    					c = 1
    					break
    			if c == 0:
    				w.append(i)
    		elif i[0] in w2:
    			for j in i:
    				if j not in w2:
    					c = 1
    					break
    			if c == 0:
    				w.append(i)
    		elif i[0] in w3:
    			for j in i:
    				if j not in w3:
    					c = 1
    					break
    			if c == 0:
    				w.append(i)
    	return w
# transfer method
solve = Solution()
print(solve.findWords(["abdfs","cccd","a","qwwewm"]))

# method 2 利用集合性质判断，快
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
    	if not words:
    		return []
    	set1 = set('qwertyuiop')
    	set2 = set('asdfghjkl')
    	set3 = set('zxcvbnm')
    	res = []
    	for i in words:
    		set_words = set(i.lower())
    		if set_words <= set1 or set_words <= set2 or set_words <= set3:
    			res.append(i)
    	return res
# transfer method
solve = Solution()
print(solve.findWords(["abdfs","cccd","a","qwwewm"]))