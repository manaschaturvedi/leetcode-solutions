'''
Link: https://leetcode.com/problems/reverse-integer/
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
[−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x):
        if x >= 0:
            return int(str(x)[::-1]) if x != 0 and -2147483648 < int(str(x)[::-1]) < 2147483647 else 0
        else:
            return int('-' + str(x)[1:][::-1]) if -2147483648 < int(str(x)[1:][::-1]) < 2147483647 else 0

sol = Solution()
print(sol.reverse(1563847412))  # 0
print(sol.reverse(120))  # 21