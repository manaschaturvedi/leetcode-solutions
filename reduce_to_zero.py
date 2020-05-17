# Reference: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        while num != 0:
        	count += 1
        	if num%2 == 1:
        		num -= 1
        	else:
        		num /=2
      	return count

obj = Solution()
print(obj.numberOfSteps(14))