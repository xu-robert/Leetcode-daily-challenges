# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 08:42:09 2020
BST range sum

just add if the number between lo and hi. Only search left if cur node is greater than L. If its smaller than L, all left nodes will be
smaller than L therefore not in range. Same on righ side

@author: Robert Xu
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        stack = [root]
        ans = 0
        while stack:
            curr = stack.pop(0)
            if curr.val <= R and curr.val >= L:
                ans += curr.val
            if curr.left and curr.val > L:
                stack.append(curr.left)
            if curr.right and curr.val < R:
                stack.append(curr.right)
        
        return ans