# Reference: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_frequency = {}
        for char in magazine:
        	if char in magazine_frequency:
        		magazine_frequency[char] += 1
        	else:
        		magazine_frequency[char] = 1
        for elem in ransomNote:
        	if elem not in magazine_frequency:
        		return False
        	else:
        		if magazine_frequency[elem] == 0:
        			return False
        		else:
        			magazine_frequency[elem] -= 1
        return True

obj = Solution()
print(obj.canConstruct('fffbfg', 'effjfggbffjdgbjjhhdegh'))
