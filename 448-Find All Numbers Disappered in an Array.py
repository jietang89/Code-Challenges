# -*- coding: utf-8 -*-
# @Author: jietang
# @Date:   2017-11-06 21:38:23
# @Last Modified by:   jietang
# @Last Modified time: 2017-11-06 22:24:30

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    ####Solution 2
        for e in nums:
        	e = abs(e)
        	nums[e-1] = - abs(nums[e-1])
       	return list(i+1 for i in range(len(nums)) if nums[i] > 0)

    ####Solution 1
        for e in nums:
        	e = abs(e)
        	if nums[e-1] > 0:
        		nums[e-1] *= -1
       	return list(i for i in range(1,len(nums)+1) if nums[i-1] > 0)

nums = [4,3,2,7,8,2,3,1]
print(Solution().findDisappearedNumbers(nums))

