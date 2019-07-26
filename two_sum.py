'''
Link: https://leetcode.com/problems/two-sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]

'''
# Approach 1: O(N)
class Solution:
    def twoSum(self, nums, target):
        '''
        Parameters:
            nums: List[int]
		target: int
 	    Output:
 	        List[int]
     	'''
        for index in range(len(nums)):
            if target - nums[index] in nums[index+1:]:
                return [index, nums.index(target-nums[index],index+1)]

sol = Solution()
print(sol.twoSum([1, 5, 5, 1], 10))  # [1, 2]

# Approach 2: O(N^2)
# class Solution:
# 	def twoSum(self, nums, target):
# 		for i in range(len(nums)):
# 			for j in range(1, len(nums)):
# 				if nums[i] + nums[j] == target and i != j:
# 					return [i, j]
