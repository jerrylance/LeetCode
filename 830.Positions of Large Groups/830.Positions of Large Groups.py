# LeetCode Solution
# Zeyu Liu
# 2019.5.8
# 830.Positions of Large Groups

from typing import List
# method 1 Straight Forward
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        res = []
        count = 1 # update the length of group
        for i in range(len(S)-1):
        	if S[i] == S[i+1]:
        		count += 1
        	else:
        		if count > 2:
        			res.append([i - count + 1, i])
        		count = 1
        if count > 2: # do this when S = 'aaa' or S = 'asdfeeeee'
        	res.append([len(S)-count ,len(S)-1])
        return res
# transfer method
solve = Solution()
print(solve.largeGroupPositions("abcdddeeeeaabbbcd"))