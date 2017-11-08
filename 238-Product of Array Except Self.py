# -*- coding: utf-8 -*-
# @Author: jietang
# @Date:   2017-11-07 17:36:32
# @Last Modified by:   jietang
# @Last Modified time: 2017-11-07 22:28:20
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] 
        for i in range(n-1):
        	res.append(res[i] * nums[i]) 
        p = 1
        for i in range(n,0,-1):
        	res[i-1] *= p
        	p *= nums[i-1]
       	return res

nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))