'''
Link: https://leetcode.com/problems/missing-number/

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''

class Solution:
    def missingNumber(self, nums):
        nums = set(nums)  # because lookups in a set are much faster as compared in lists
        max_num = max(nums)
        for i in range(max_num+1):
            if i not in nums:
                return i
        return i+1

sol = Solution()
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))