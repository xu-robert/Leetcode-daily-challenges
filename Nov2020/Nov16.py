# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:26:19 2020
Longest mountain array

Enumerate cases:
    
    if A[i] < A[i-1]:
        if we are following an increasing slope: add 1 to cur mountain
    
    if A[i] == A[i-1] slope is no longer increasing
    
    if A[i] > A[i-1]:
        if slope was just decreasing: start of a new mountain array so cur mountain = 2
        if slope was just increasing: add to cur mountain
        
@author: Robert Xu
"""
class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        if len(A) < 3: return 0
        
        cur_mountain = 0
        max_mountain = 0
        
        inc_slope_found = False
        decreasing = True
        
        for i in range(1, len(A)):
            
            if A[i] < A[i-1]:
                
                decreasing = True
                
                if inc_slope_found:
                    
                    cur_mountain += 1
                    max_mountain = max(max_mountain , cur_mountain)
            
            elif A[i] > A[i-1]:
                
                inc_slope_found = True
                
                if decreasing == True:
                    
                    cur_mountain = 2
                
                else:
                    
                    cur_mountain += 1
                
                decreasing = False
            
            else:
                inc_slope_found = False
            
        return max_mountain