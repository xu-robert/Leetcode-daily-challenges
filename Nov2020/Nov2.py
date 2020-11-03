# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 21:46:11 2020

Ok yes I cheated and used builtin sort :)


@author: Robert Xu
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return None
        
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        
        nodes.sort(key = lambda x: x.val)
        
        for i in range(len(nodes)-1):
            
            nodes[i].next = nodes[i+1]
        
        nodes[-1].next = None
        
        return nodes[0]