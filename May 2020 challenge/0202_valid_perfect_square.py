class Solution(object):
    def isPerfectSquare(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		if num%2 == 0:
			for elem in range(2, num/2+1, 2):
				if elem*elem == num:
					return True
			return False
		else:
			if num == 1:
				return True
			for elem in range(1, num/2+1, 2):
				print(elem)
				if elem*elem == num:
					return True
			return False

obj = Solution()
print(obj.isPerfectSquare(1))