# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 09:00:17 2020

Add two numbers II

Store the nodes in a stack, so that when we pop from the stack, each node represents the same
position (ones, tens, hundreds). Add some conditions in case one list is shorter than the other
and how to deal with a one bein carried over to the last node

@author: Robert Xu
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        s1, s2 = [],[]
        
        while l1:
            s1.append(l1)
            l1 = l1.next
        
        while l2:
            s2.append(l2)
            l2 = l2.next
        
        carry = 0
        prev = None
        
        while s1 or s2:
            
            a = s1.pop() if s1 else ListNode(0)
            b = s2.pop() if s2 else ListNode(0)
            new_val = a.val+b.val+carry
            carry, new_val = divmod(new_val, 10)
            new_node = ListNode(new_val, prev)
            prev = new_node
        
        if carry == 1: return ListNode(1, prev)
        return prev
