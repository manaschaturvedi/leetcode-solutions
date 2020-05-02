# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(version):
    if version == 4:
        return True
    else:
        return False


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start < end:
            mid = (start+end)/2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid+1
        return start

obj = Solution()
print(obj.firstBadVersion(5))