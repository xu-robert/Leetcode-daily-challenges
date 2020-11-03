# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 08:32:08 2020

Consecutive Characters

@author: Robert Xu
"""

class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        curpow = maxpow = 1
        
        for i in range(1, len(s)):
            
            if s[i] == s[i-1]:
                
                curpow += 1
                maxpow = max(curpow, maxpow)
            
            else:
                curpow = 1
        
        return maxpow

a = Solution()
b = a.maxPower("abbcccddddeeeeedcba")