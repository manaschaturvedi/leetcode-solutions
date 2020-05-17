# Reference: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320/

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
        	return 0
        index = 0
        final = -1
        factored_chars = []
        while index < len(s):
        	if s[index] not in s[index+1:] and s[index] not in factored_chars:
        		final = index
        		break
        	factored_chars.append(s[index])
        	index += 1
        return final

obj = Solution()
print(obj.firstUniqChar("cc"))