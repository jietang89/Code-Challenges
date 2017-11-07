# -*- coding: utf-8 -*-
# @Author: jietang
# @Date:   2017-11-06 20:02:10
# @Last Modified by:   jietang
# @Last Modified time: 2017-11-06 22:17:10

class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
    ####Solution 3
        l = list(range(1,n+1))
        a = 1
        b = k+1
        for i in range(k+1):
        	if i % 2 == 0:
        		l[i] = a
        		a += 1
        	else:
        		l[i] = b
        		b -= 1
        return l

    # ####Solution 2
    #     l = list(range(1,n+1))
    #     for i in range(k+1):
    #     	if i % 2 == 0:
    #     		l[i] = i//2+1
    #     	else:
    #     		l[i] = k+1-i//2
    #     return l

    # ####Solution 1
    #     a = range(1,k//2+2)
    #     b = range(k+1,k//2+1,-1)
    #     if k % 2 == 1:
    #     	l = sum(list(map(list,zip(a,b))),[])
    #     else:
    #     	l = sum(list(map(list,zip(a[:-1],b))),[])+[a[-1]]

    #     return l + list(range(k+2,n+1))

print(Solution().constructArray(5,3))



