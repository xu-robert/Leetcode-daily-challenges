# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 09:28:33 2020

House Robber III:
    
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

Solution is commented: we do postorder traversal

@author: Robert Xu
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            
            if root == None:
                
                return (0, 0)
            
            #rob left: max we can get if we rob the left child
            #rob grand left: max we can get if we dont rob left child
            
            can_rob_left, dont_rob_left = helper(root.left)
            
            can_rob_right, dont_rob_right = helper(root.right)
            
            #If we rob the root, we cant rob left and right child
            rob_root = root.val + dont_rob_left + dont_rob_right
            
            #if we dont rob the root, we rob the left and right child
            dont_rob_root = can_rob_left + can_rob_right
            
            #max of both scenarios is the most we can get at the root, regardless of
            #whether we rob or dont rob the root
            
            best = max(rob_root, dont_rob_root)
            
            #the calling function receives best either as rob left or rob right. 
            #at the calling function root, if we choose to rob the root, we cant get this value
            #If we dont rob the root, the calling function receives dont_rob_root as either
            #rob grand left or rob grand right
            
            #note that best can be the same as dont_rob_root, meaning its better to not rob
            #the root. If both tuple values are the same, it means its better if we leave the
            #root alone, and we can still rob the roots children. A better phrasing for rob_left
            #and rob_right is can rob left and can rob right, indicating that we dont 
            #necessarily rob the right and left roots, but we have the option to do so
            # if it leads to a higher amount robbed
            
            return (best, dont_rob_root)
        
        return helper(root)[0]
        
        