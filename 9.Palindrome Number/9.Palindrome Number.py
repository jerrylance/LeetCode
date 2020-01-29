# LeetCode Solution
# Zeyu Liu
# 2019.1.29
# 9.Palindrome Number

# method 1 切片，正反切对比,速度快
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x[::] == x[::-1]:
            return True
        else:
            return False
# transfer method
solve = Solution()
print(solve.isPalindrome(-123))

# method 2 方法一进一步优化
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x = str(x)
            if x[::] == x[::-1]:
                return True
            else:
                return False
# transfer method
solve = Solution()
print(solve.isPalindrome(-123))

# method 3 方法二进一步优化
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x = str(x)
            return x[::-1] == x
# transfer method
solve = Solution()
print(solve.isPalindrome(-123))