'''
Link: https://leetcode.com/problems/non-decreasing-array/
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
'''

'''
Approach: If the current element is greater than the next one, we can do one of two things: 
- replace the current element with the value of the next one
- replace the next element with the value of the current one

So, we would try doing both for the first instance of the current element being greater than the next one
while running a loop through the list by maintaining two different versions of the list

If the resultant list in either of the two cases is equal to the sorted list, return True, else False
'''
class Solution:
    def checkPossibility(self, nums):
        one = nums[:]
        two = nums[:]
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                one[i] = nums[i+1]
                two[i+1] = nums[i]
                break
        return one == sorted(one) or two == sorted(two)
                
sol = Solution()
print(sol.checkPossibility([-1, 4, 2, 3, 1]))
        

# Solution that didn't work for 7 out of the 325 test cases:
'''
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        i = 0
        mismatch_count = 0
        if len(nums) > 1:
            while i < len(nums):
                if mismatch_count > 1:
                    return False
                else:
                    if i == 0:
                        if nums[i] > nums[i+1]:
                            nums[i] = nums[i+1]
                            mismatch_count += 1
                    elif i+1 == len(nums):
                        if nums[i] < nums[i-1]:
                            mismatch_count += 1   
                    elif nums[i] < nums[i-1] or nums[i] > nums[i+1]:
                        if nums[i] < nums[i-1]:
                            nums[i] = nums[i-1]
                            mismatch_count += 1
                        if nums[i] > nums[i+1] and i+2 != len(nums):
                            if nums[i] >=  nums[i-1]:
                                nums[i+1] = nums[i]
                            else:
                                nums[i] = nums[i-1]
                            mismatch_count += 1
                    i += 1
        else:
            return True
        return True if mismatch_count <= 1 else False
'''