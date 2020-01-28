# LeetCode Solution
# Zeyu Liu
# 2019.1.28
# 5.Longest Palindromic Substring

# method 1 利用切片在字符串上水平遍历，判断每个切片和自身反转是否相同，若相同输出此时切片，速度太慢
class Solution:
    def longestPalindrome(self, s: str) -> str:

    	longestPalins = []
    	if s == "": #特殊情况
    		return ""
    	for i in range(len(s)):
    		for j in range(1+i,len(s)+1):#注意嵌套循环的范围
    			subslice = s[i:j]
    			if subslice[::-1] == subslice:
    				longestPalins.append(subslice)
    	return(max(longestPalins, key = len))

# transfer method
solve = Solution()
print(solve.longestPalindrome("asdfede"))

# method 2 方法1的优化
class Solution:
    def longestPalindrome(self, s: str) -> str:

    	longestPalins = []
    	maxlength = 0
    	if s == "": #特殊情况
    		return ""
    	for i in range(len(s)):
    		for j in range(1+i,len(s)+1):#注意嵌套循环的范围
    			subslice = s[i:j]
    			if len(subslice) > maxlength:
    				if subslice[::-1] == subslice:
    					longestPalins.append(subslice)
    					maxlength = len(subslice)
    	return(max(longestPalins, key = len))

# transfer method
solve = Solution()
print(solve.longestPalindrome("asdfede"))

# method 3 从中间到两边查找，常规方法,速度较快
class Solution:
    def longestPalindrome(self, s: str) -> str:
                # palindrome can be even or odd....
        # every palindrome must be centred on a pair or on one letter
        if len(s) < 2 and s == s[::-1]:
            return s
        ans = ""
        def helper(lo, hi):
            # returns longest palindrome centred at s[lo + 1:hi]
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]: # overshoots edges
                lo -= 1
                hi += 1
            return s[lo+1:hi]
            
        for i in range(len(s)):
            ans = max(ans, helper(i, i), key=len)  
            ans = max(ans, helper(i, i + 1), key=len)
        return ans
# transfer method
solve = Solution()
print(solve.longestPalindrome("asdfede"))


# method 4 方法3进一步优化，速度最快
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1: return s
        start, maxlen, i = 0, 1, 0
        while i < n:
            if n-i <= maxlen/2: break
            j, k = i, i 
            while k < n-1 and s[k]==s[k+1]:
                k+=1
            i = k+1
            while k < n-1 and j and s[k+1]==s[j-1]:
                k, j = k+1, j-1
            if k-j+1 > maxlen:
                start, maxlen = j, k-j+1
        return s[start:start + maxlen]
# transfer method
solve = Solution()
print(solve.longestPalindrome("asdfede"))