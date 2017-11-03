# -*- coding: utf-8 -*-
# @Author: jietang
# @Date:   2017-11-02 20:05:02
# @Last Modified by:   jietang
# @Last Modified time: 2017-11-02 20:56:58

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # ####Solution 3
    #     count = 0
    #     max_count = 0

    #     for e in nums:
    #     	if e == 1:
    #     		count += 1
    #     		max_count = max(max_count,count)
    #     	emax_count = max(max_count,count)max_count = max(max_count,count)max_count = max(max_count,count)max_count = max(max_count,count)lse:
    #     		count = 0

    #     return max(count,max_count)

    ####Solution 2:
    	# Use `map` and `join`
        return max(map(len, ''.join(map(str, nums)).split('0')))
   

    # ####Solution 1
    #     count = 0
    #     max_count = 0

    #     for e in nums:
    #     	if e == 1:
    #     		count += 1
    #     	else:
    #     		if max_count < count:
    #     			max_count = count
    #     		count = 0

    #     return max(count,max_count)

nums = [1,1,0,1,1,1]        
print(Solution().findMaxConsecutiveOnes(nums))
