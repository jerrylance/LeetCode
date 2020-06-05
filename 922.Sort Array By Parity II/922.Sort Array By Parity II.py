# LeetCode Solution
# Zeyu Liu
# 2019.5.5
# 922.Sort Array By Parity II

from typing import List
# method 1 O(n)space, one pointer, even和odd分别作为索引迭代
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        even = 0
        odd = 1
        for i in A:
        	if i % 2 == 0:
        		res[even] = i
        		even += 2
        	else:
        		res[odd] = i
        		odd += 2
        return res
# transfer method
solve = Solution()
print(solve.sortArrayByParityII([4,2,5,7]))

# method 2 O(1)space, two pointer, 根据当前元素奇偶性，互换i和j即可
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i, j, L = 0, 1, len(A)              # i - even index, j - odd index
        while j < L:                        # (L - 1) is odd, j can reach the last element, so this condition is enough
            if A[j] % 2 == 0:               # judge if the value on odd indices is odd
                A[j], A[i] = A[i], A[j]     # if it is even, exchange the values between index j and i
                i += 2                      # even indices get a right value, then i pointer jump to next even index
            else:
                j += 2                      # if it is odd, odd indices get a right value, then j pointer jump to next odd index
        return A
# transfer method
solve = Solution()
print(solve.sortArrayByParityII([4,2,5,7]))

# method 3 奇偶分治法，最后合并
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        odd = []
        even = []
        for i in A:
            if i % 2 != 0:
                odd.append(i)
            else:
                even.append(i)
        res[0::2] = even
        res[1::2] = odd
        return res
# transfer method
solve = Solution()
print(solve.sortArrayByParityII([4,2,5,7]))