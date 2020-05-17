# Reference: https://leetcode.com/problems/count-of-smaller-numbers-after-self/

import bisect


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        final = [0] * len(nums)
        sorted_li = []
        for index in range(len(nums)-1, -1, -1):
        	sorted_index = bisect.bisect_left(sorted_li, nums[index])
        	final[index] = sorted_index
        	sorted_li.insert(sorted_index, nums[index])
        return final

obj = Solution()
print(obj.countSmaller([5,2,6,1]))

# Initial approach: passed 15/16 cases - O(n^2)

# class Solution(object):
#     def countSmaller(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         final = []
#         index = 0
#         while index < len(nums):
#         	count = 0
#         	for elem in nums[index+1:]:
#         		if nums[index] > elem:
#         			count += 1
#         	final += [count]
#         	index += 1
#         return final

