# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 14:08:21 2020
 Maximum Difference Between Node and Ancestor
 
 preorder traverse the tree, pass the min and max ancestor to the children, when we get to the
 child evaluate the difference between its val and max/min ancestor, and update ans if its 
 greater
@author: Robert Xu
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        stack = [(root, root.val, root.val)]
        
        while stack:
            
            cur, max_ancestor, min_ancestor = stack.pop()
            
            ans = max(ans, abs(max_ancestor - cur.val), abs(min_ancestor - cur.val))
                      
            if cur.left:
                
                stack.append((cur.left, max(cur.val, max_ancestor), min(cur.val, min_ancestor)))
            
            if cur.right:
                      
                stack.append((cur.right, max(cur.val, max_ancestor), min(cur.val, min_ancestor)))
        
        return ans
        