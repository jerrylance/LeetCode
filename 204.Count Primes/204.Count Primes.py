# LeetCode Solution
# Zeyu Liu
# 2019.2.28
# 204.Count Primes

from typing import List
# method 1 埃拉托斯特尼筛法 Sieve of Eratosthenes (这道题有小坑，不包括n)
class Solution:
    def countPrimes(self, n: int) -> int:
    	if n < 2:
    		return 0
    	l = [1] * n  # give a strike list
    	l[0] = 0
    	l[1] = 0
    	for i in range(2,int(n**0.5) + 1):
    		if l[i] == 1:
    			for j in range(i*i,n,i):
    				l[j] = 0
    	return sum(l) # return numbers of True
# transfer method
solve = Solution()
print(solve.countPrimes(10))

# method 2 方法1优化，最快, 这道题用其他求素数方法，会超时
class Solution:
    def countPrimes(self, n: int) -> int:
    	if n < 2:
    		return 0
    	l = [1] * n  # give a strike list
    	l[0] = 0
    	l[1] = 0
    	for i in range(2,int(n**0.5) + 1):
    		if l[i] == 1:
    			l[i*i:n:i] = (((n-1)-(i*i))//i + 1) * [0] # 利用切片一次性赋值，因为是等差数列，calculate the numbers of 0
    			#l[i*i:n:i] = [0] * len(l[i*i:n:i]) # 换成这一句，速度会慢100ms
    	return sum(l) # return numbers of True
# transfer method
solve = Solution()
print(solve.countPrimes(10))