# LeetCode Solution
# Zeyu Liu
# 2019.4.21
# 804.Unique Morse Code Words

from typing import List
# method 1 set(), ord()
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morsecode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        w = set()
        for i in words:
        	s = ''
        	for j in i:
        		s += (morsecode[ord(j)-ord('a')])
        	w.add(s)
        return len(w)
# transfer method
solve = Solution()
print(solve.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))

# method 2 hash table,常规
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morsecode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        w = []
        for i in words:
        	s = ''.join(morsecode[ord(j) - 97] for j in i)
        	if s not in w:
        		w.append(s)
        return len(w)
# transfer method
solve = Solution()
print(solve.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))