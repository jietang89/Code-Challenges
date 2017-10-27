#461. Hamming Distance

class Solution:
	def hammingDistance(self,x,y):
		"""
		:type x: int
		:type y: int
		:rtype: int
		"""
	####Solution 1
		count = 0
		while x != 0 or y != 0:
			if x % 2 != y % 2:
				count += 1
			x = x // 2
			y = y // 2
		return count
	####Solution 2
		return bin(x^y).count('1')
		# ^ is XOR
print(Solution().hammingDistance(1,4))