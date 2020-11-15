# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 23:24:31 2020
Poor pigs

subset problem

@author: Robert Xu
"""
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        
        if buckets == 1: return 0
        
        n = (minutesToTest/minutesToDie)+1
        
        i = 1
        num = n**1
        
        while num < buckets:
            i += 1
            num = n**i
        
        return i
            