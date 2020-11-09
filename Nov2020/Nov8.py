# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 12:42:28 2020
563. Binary Tree Tilt

classified as easy but i had a hard time with it. We modify the tree values as we do a postorder
traversal. Each nodes new value is the sum of nodes in its left tree and right tree. Then we
take abs(left - right) if they exist and add to a global ans variable. get_sum_tree does all in
one function.

@author: Robert Xu
"""
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def get_sum_tree(root):
            
            if root == None: return 0
            
            l = get_sum_tree(root.left)
            r = get_sum_tree(root.right)
            root.val += l+r
            self.ans += abs((root.left.val if root.left else 0) - (root.right.val if root.right else 0))
            return root.val
        
        get_sum_tree(root)
        return self.ans