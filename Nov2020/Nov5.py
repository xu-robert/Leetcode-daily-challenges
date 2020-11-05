# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 09:15:41 2020

1217. Minimum Cost to Move Chips to The Same Position

free for odds to move to odds, and evens to move to evens. Cost for an odd to move to any even is 1, and vice versa.
Just find out if its better to finish on an even or odd spot.

@author: Robert Xu
"""
class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        if len(position) == 1:
            return 0
        
        odds = evens = 0
        
        for pos in position:
            
            if pos % 2 == 0:
                odds += 1
            
            else:
                evens += 1
        
        return min(odds, evens)
            