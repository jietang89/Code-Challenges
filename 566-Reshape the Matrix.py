# -*- coding: utf-8 -*-
# @Author: jietang
# @Date:   2017-11-01 22:42:59
# @Last Modified by:   jietang
# @Last Modified time: 2017-11-02 00:01:25
import numpy as np
import itertools
class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
    ####Solution4:
    	# use `itertools`
        if len(nums)*len(nums[0]) != r*c: return nums
        it = itertools.chain(*nums)
        return [list(itertools.islice(it, c)) for _ in range(r)]
        	
    # ####Solution3:
    # 	# use `zip`
    #     if len(nums)*len(nums[0]) != r*c: return nums
        
    #     flat = sum(nums,[])
    #     tuples = zip(*([iter(flat)] * c))
    #     return map(list,tuples)
    # ####Solution2:
    # 	# Directly use `Numpy`
    # 	try:
    # 		return np.reshape(nums,(r,c)).tolist()
    # 	except:
    # 		return nums
    # ####Solution 1
    #     ro = len(nums)
    #     co = len(nums[0])
    #     l1 = []
    #     if ro * co != r * c:
    #     	return nums
    #     for l in nums:
    #     	for e in l:
    #     		l1.append(e)
    #     return list(l1[i*c:(i+1)*c] for i in range(r))

nums = [[1,2],[3,4],[5,6]]
r,c = 3,2
print(Solution().matrixReshape(nums,r,c))
