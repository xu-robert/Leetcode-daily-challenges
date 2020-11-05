# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 10:51:10 2020
 
Minimum Height Trees

Intuition: eat away the leaf nodes until only one or two nodes are remaining. The max number of min height trees is 2.
The leaf nodes can never be part of a min height tree if more than 2 nodes. Think about it like a physical tree where
the nodes are marbles tied together with string. The min height tree is the marble with the least length of string dangling.
This can never be the leaf nodes, so we remove them and keep trying to solve the smaller problem

@author: Robert Xu
"""

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: return [0]
        
        graph = {i:set() for i in range(n)}
        
        for u, v in edges:
            
            graph[u].add(v)
            graph[v].add(u)
        
        leaves = [i for i in graph if len(graph[i]) == 1]
        
        
        while len(graph) > 2:
        
            new_leaves = []    
        
            for leaf in leaves:
                
                parent = graph.pop(leaf).pop()
                graph[parent].remove(leaf)
                
                if len(graph[parent]) == 1:
                    new_leaves.append(parent)
            
            leaves = new_leaves
        
        return [key for key in graph]

a = Solution()
b = a.findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]])
            