# Reference: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for stone in S:
        	if stone in J:
        		count += 1
        return count


J = "aA"
S = "aAAbbbb"
obj = Solution()
print(obj.numJewelsInStones(J, S))
