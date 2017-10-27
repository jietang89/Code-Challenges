# -*- coding: utf-8 -*-
# @Author: jietang
# @Date:   2017-10-27 17:19:23
# @Last Modified by:   jietang
# @Last Modified time: 2017-10-27 17:41:53

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
    # ####Solution 1
    #     count1 = 0
    #     count2 = 0

    #     for i in moves:
    #     	if i not in "UDLR": print ("Value is Wrong")
    #     	if i == "U": count1 += 1
    #     	elif i == "D": count1 -= 1
    #     	elif i == "L": count2 += 1
    #     	else: count2 -= 1
    #     return count1 == count2 == 0
    ####Solution 2
        # return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
    ####Solution 3 
    	direct = {'U':1,'D':-1,'L':1j,'R':-1j}
    	return 0 == sum(direct[m] for m in moves)


print(Solution().judgeCircle("LL"))