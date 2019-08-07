'''
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        sorted_li = sorted(nums1 + nums2)
        if len(sorted_li) % 2 == 0:
            return float(sorted_li[int(len(sorted_li)/2)] + sorted_li[int(len(sorted_li)/2)-1])/2
        else:
            return float(sorted_li[int(len(sorted_li)/2)])

sol = Solution()
print(sol.findMedianSortedArrays([1, 2], [3, 4]))