# Reference: https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        final = []
        for num in nums:
        	count = 0
        	for current_elem in nums:
        		if current_elem < num and current_elem != num:
        			count += 1
        	final.append(count)
       	return final

obj = Solution()
print(obj.smallerNumbersThanCurrent([8,1,2,2,3]))