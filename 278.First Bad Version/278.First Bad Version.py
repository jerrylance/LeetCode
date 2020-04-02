# LeetCode Solution
# Zeyu Liu
# 2019.3.17
# 278.First Bad Version

from typing import List

# method 1 binary lterative，快
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
def isBadVersion(version):
    if version >= 4:
        return True
    else:
        return False
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid) == True:
                r = mid
            else:
                l = mid + 1
        return r
# transfer method
solve = Solution()
print(solve.firstBadVersion(5))

# method 2 recursive
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binarysearch(1,n)
    def binarysearch(self,l,r):
        if l == r:
            return l
        mid = (l + r)//2
        if isBadVersion(mid) == True:
            return self.binarysearch(l,mid)
        else:
            return self.binarysearch(mid+1,r)
# transfer method
solve = Solution()
print(solve.firstBadVersion(5))