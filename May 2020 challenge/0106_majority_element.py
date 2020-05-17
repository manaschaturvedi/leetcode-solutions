# Reference: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        char_count = {}
        for elem in nums:
        	if elem in char_count:
        		char_count[elem] += 1
        	else:
        		char_count[elem] = 1
        for key, value in char_count.items():
        	if value > len(nums)/2:
        		return key

obj = Solution()
print(obj.majorityElement([3,2,3]))