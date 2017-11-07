# -*- coding: utf-8 -*-
# @Author: jietang
# @Date:   2017-11-06 22:25:55
# @Last Modified by:   jietang
# @Last Modified time: 2017-11-06 23:07:19

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p = 0

        for i in range(len(nums)):
        	if nums[i] != 0:
        		if i > p:
        			nums[p] = nums[i]
        		p += 1
        nums[p:] = [0]*(len(nums[p:]))
       	return nums

nums = [0, 1] * 200000
print(Solution().moveZeroes(nums))

        		
