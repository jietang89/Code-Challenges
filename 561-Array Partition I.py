# -*- coding: utf-8 -*-
# @Author: jietang
# @Date:   2017-11-01 21:59:40
# @Last Modified by:   jietang
# @Last Modified time: 2017-11-01 22:42:08

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        assert len(nums) % 2 == 0 , "Not Valid Array"
        nums.sort()
        return sum(nums[::2])
nums = [1,4,3,2]
print(Solution().arrayPairSum(nums))