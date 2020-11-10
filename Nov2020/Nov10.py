# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 08:55:34 2020
Flipping an image

Reverse each row and invert at the same time. easy peasy

@author: Robert Xu
"""
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            
            i, j = 0, len(A)-1
            
            while i <= j:
                
                row[i],row[j] = 1-row[j], 1-row[i]
                
                i += 1
                j -= 1
        
        return A