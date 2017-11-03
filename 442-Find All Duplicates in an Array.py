# -*- coding: utf-8 -*-
# @Author: jietang
# @Date:   2017-11-02 19:31:54
# @Last Modified by:   jietang
# @Last Modified time: 2017-11-02 20:03:51
from collections import defaultdict
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    ####Solution 2:
    	# O(1) Space with condition: 1<=a[i]<=n
        res = []
        for x in nums:
        	if nums[abs(x)-1]<0:
        		res.append(abs(x))
        	else:
        		nums[abs(x)-1] *= -1
        return res
    # ####Solution 1
    #     d = defaultdict(int)
    #     for e in nums:
    #     	d[e] += 1
    #     return list(e for e in d if d[e] == 2)
        
nums = [4,3,2,7,8,2,3,1]
print(Solution().findDuplicates(nums))