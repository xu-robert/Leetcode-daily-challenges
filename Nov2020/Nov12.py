# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 16:09:49 2020

Permutations II: same idea as letter tiles. Implement iterative postorder traversal of a recursion
tree. Each time we visit a new node, we decrement the count of the last element we put on the
path. When we have a path same length as array, we found a permutation. Backtrack step is
when we visit a node already visited, and increment the count of the last element added. This allows
us to pick that element for next visited paths. 

@author: Robert Xu
"""
from collections import Counter

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        counts = Counter(nums)
        stack = [([n], False) for n in counts]
        res = []
        
        while stack:
            path, visited = stack.pop()
            
            if len(path) == len(nums):
                res.append(path)
                continue
            
            if visited == True:
                counts[path[-1]] += 1
            
            else:
                stack.append((path, True))
                counts[path[-1]] -= 1
                
                for c in counts:
                    if counts[c] > 0:
                        stack.append((path+[c], False))
            
        return res

a = Solution()
b = a.permuteUnique([1,3,2,1])
                
                
            
            