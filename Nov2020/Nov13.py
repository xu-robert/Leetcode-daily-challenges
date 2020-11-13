# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:55:27 2020
Populating Next Right Pointers in Each Node

as we traverse the current level, we link the children using the following logic:
    
    if the current node has a left, it has a right (since perfect tree) and we link l to r
    if the current node has a next, then cur.right points to next.left
    
    if the current node has no right, then we have reached the end of the level and move to nxt,
    which is defined at the start of each level as the left node of the leftmost node in current level
    
    
@author: Robert Xu
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        if root == None: return None
        
        cur = root
        
        nxt = cur.left
        
        while cur.left:
            
            cur.left.next = cur.right
            
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            
            else:
                cur = nxt
                nxt = cur.left
        
        return root