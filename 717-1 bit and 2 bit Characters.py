# -*- coding: utf-8 -*-
# @Author: jietang
# @Date:   2017-11-02 22:17:07
# @Last Modified by:   jietang
# @Last Modified time: 2017-11-02 22:48:04

class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        try:
        	n = bits[::-1][1:].index(0)
        except:
        	n = len(bits) - 1
        # print(n)
        return n % 2 == 0

bits = [1,1,1,1,0,1,0]
print(Solution().isOneBitCharacter(bits))