# -*- coding: utf-8 -*-
# @Author: jietang
# @Date:   2017-10-27 22:59:44
# @Last Modified by:   jietang
# @Last Modified time: 2017-11-01 21:57:07

import collections 

class Solution:
	def findShortestSubArray(self, nums):

	# ####Solution 4:
	# 	# Brute Force Method (not good)
	# 	return min((-nums.count(x),len(nums)-nums.index(x)-nums[::-1].index(x)) for x in set(nums))[1]




	# ####Solution 3:
	# 	# Use `defaultdict()`
	# 	map = collections.defaultdict(list)
	# 	for i in range(len(nums)):
	# 		map[nums[i]].append(i)
	# 	return min((-len(list),list[-1]-list[0]+1) for list in map.values())[1]



  #   ####Solution 2: 
  #   	# Use `Counter()` and `setdefault()`
		# c = collections.Counter(nums)
		# # print (c)
		# first, last = {},{}
		# for i,v in enumerate(nums):
		# 	first.setdefault(v,i)
		# 	last[v] = i
		# degree = max(c.values())
		# return min(last[v] - first[v] + 1 for v in c if c[v] == degree)
    


    # ####Solution 1
    #     degree = []
    #     length = []
        
    #    	indexl = sorted(range(len(nums)),key = nums.__getitem__)
    #    	l = [indexl[0]]
    #    	d = 1
    #    	for i in range(1,len(nums)):
    #    		if nums[indexl[i]] == nums[indexl[i-1]]:
    #    			d += 1
    #    			l.append(indexl[i])
    #    		else:
    #    			degree.append(d)
    #    			length.append(l)
    #    			d = 1
    #    			l = [indexl[i]]
    #    	degree.append(d)
    #    	length.append(l)

    #    	ml = len(nums)
    #    	m = max(degree)
    #    	for i in range(len(degree)):
    #    		if degree[i] == m:
    #    			diff = max(length[i]) - min(length[i]) + 1
    #    			if diff < ml:
    #    				ml = diff
    #    	return ml





print(Solution().findShortestSubArray([1,2,2,3,1,4,2]))