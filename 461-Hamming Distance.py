# -*- coding: utf-8 -*-
# @Author: jietang
# @Date:   2017-10-27 16:52:08
# @Last Modified by:   jietang
# @Last Modified time: 2017-10-27 17:07:03


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