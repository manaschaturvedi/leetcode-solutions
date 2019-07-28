'''
Link: https://leetcode.com/problems/group-anagrams/
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

'''
Work in progress. The solution is failing for this test case:

Input
["",""]
Output
[[""]]
Expected
[["",""]]
'''

class Solution:
    def groupAnagrams(self, strs):
        final = []
        for i in range(len(strs)):
            li = [strs[i]]
            for j in range(len(strs)):
                if set(strs[i]) == set(strs[j]) and strs[i] != strs[j]:
                    if strs[j] not in li:
                        li.append(strs[j])
            final.append(li)
        final = [set(elem) for elem in final]
        output = []
        for elem in final:
            if elem not in output:
                output.append(elem)
        return [list(elem) for elem in output]

sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
        