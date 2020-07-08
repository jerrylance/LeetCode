# LeetCode Solution
# Zeyu Liu
# 2019.5.22
# 762.Prime Number of Set Bits in Binary Representation

from typing import List
# method 1 bin(),count()，常规法
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        # from the questions, we know the note:
        # L, R will be integers L <= R in the range [1, 10^6].
        # R - L will be at most 10000.
        # so the prime numer only include:
        prime = [2,3,5,7,11,13,17,19] 
        count = 0
        for i in range(L,R+1):
        	if bin(i).count('1') in prime:
        		count += 1
        return count
# transfer method
solve = Solution()
print(solve.countPrimeSetBits(10, 15))

# method 2 大神的binomial coefficients高级方法，fast count()，需要进一步理解，最快
def binomial(n, k, cache={}):
    if k == 0: return 1
    if (n, k) not in cache:
        cache[n, k] = binomial(n-1, k-1) * n // k
    return cache[n, k]
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        return self.fast_count(R+1) - self.fast_count(L)    
    def fast_count(self, N):
        S = bin(N)
        B = [len(S) + ~i for i, b in enumerate(S) if b == '1']
        res = 0
        for p in [2, 3, 5, 7, 11, 13, 17, 19]:
            if B[0] < p: 
            	break
            for i in range(min(p+1, len(B))):
                n = B[i]
                k = p-i
                if n < k: 
                	break
                res += binomial(n, k)
        return res
# transfer method
solve = Solution()
print(solve.countPrimeSetBits(10, 15))