# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 10:09:13 2020
 Merge Intervals

Sort by the first element. Then iterate through the nums list, starting with start = interval[0], 
end = interval[1]. Let a be the start of the current interval, b is the end of current interval.
Start is the start of our temporary interval, end is the end of temp interval.

If a less than or equal to end, we are guaranteed that it overlaps with our temp interval because of
sorting: a >= start, and if a less than or equal to end, there is an overlap. So we may need to
update the end of our temp interval. If a greater than end, then there is definitely no overlap. SO the
temp interval becomes part of the solution, and we start a new temp interval with a and b. At the end,
we need to append whatever start, end is to the result, because either 1: we updated the end if a <= end,
or 2: we started a new interval because a > end. In any case, the last interval did not get added to res

We can clean up that last time but im too lazy :P

@author: Robert Xu
"""
class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x: x[0])
        res = []
        start, end = intervals[0]

        for a, b in intervals[1:]:
            if a <= end:
                end = max(end, b)
            
            elif a > end:
                res.append([start, end])
                start, end = a, b
        
        res.append([start, end])
        return res