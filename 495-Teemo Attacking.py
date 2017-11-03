# -*- coding: utf-8 -*-
# @Author: jietang
# @Date:   2017-11-02 22:57:54
# @Last Modified by:   jietang
# @Last Modified time: 2017-11-02 23:26:54

class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
    ####Solution 2
    	if timeSeries:
        	return sum(min(duration,timeSeries[i]-timeSeries[i-1]) for i in range(1,len(timeSeries)))+duration
    	else: return 0
    # ####Solution 1
    #     n = len(timeSeries)
    #     overlap = 0
    #     for i in range(1,n):
    #     	gap = timeSeries[i] - timeSeries[i-1]
    #     	if gap < duration:
    #     		overlap += duration - gap
    #     return n*duration-overlap

timeSeries = [1,5,6]
duration = 2
print(Solution().findPoisonedDuration(timeSeries,duration))