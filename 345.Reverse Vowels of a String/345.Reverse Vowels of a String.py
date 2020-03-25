# LeetCode Solution
# Zeyu Liu
# 2019.3.11
# 345.Reverse Vowels of a String

from typing import List
# method 1 Two-point method, 注意转换成列表才能有赋值操作,0(n)
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowel = ['a', 'e', 'i', 'o', 'u']
        left = 0
        right = len(s)-1
        while left < right:
            if s[left].lower() in vowel:
                if s[right].lower() in vowel:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1 
        return ''.join(s)
# transfer method
solve = Solution()
print(solve.reverseVowels("leetcode"))

# method 2 recursive, pop()
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u']
        v = []
        s1 = ''
        for i in s:
            if i.lower() in vowel:
                v.append(i)
        for i in s:
            if i.lower() in vowel:
                s1 += v.pop()
            else:
                s1 += i
        return s1
# transfer method
solve = Solution()
print(solve.reverseVowels("leetcode"))

# method 3 方法1优化, 使用字典{}代替列表[]，速度提高50%
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] not in vowel:
                left += 1
            elif s[right] not in vowel:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)
# transfer method
solve = Solution()
print(solve.reverseVowels("leetcode"))