# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 08:53:00 2020

1283. Find the Smallest Divisor Given a Threshold
Binary search

@author: Robert Xu
"""
import math

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        
        def eval_sum(mid): return sum(math.ceil(n/mid) for n in nums)
            
        mx, mn = max(nums), 1
        
        while mn < mx:
            mid = (mn + mx)//2
            s = eval_sum(mid)
            
            if s <= threshold:
                mx = mid
            
            else:
                mn = mid+1
            
        return mn
    
a = Solution()
b = a.smallestDivisor(nums = [1,2,5,9], threshold = 6)