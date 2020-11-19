# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 08:46:43 2020
Decode String

Keep 2 stacks, one for letters, and one for multipliers. Also keep a temp variable to store the multiplier
as we build in from individual digits. Loop through the string. if the current char is a digit, add it
to our temp multiplier. If char is '[', then we know we reach the end of our multiplier, so convert
our temp multiplier to num and add it to num stack. If char is ']', then we reached the last char for 
the multiplier on top of the num stack to be applied, so we apply it to our current string on top of
our other stack, and merge it back on to the stack. 
@author: Robert Xu
"""
class Solution(object):
    def decodeString(self, s):
        
        stack = ['']
        num = []
        nums = []
        
        for char in s:
            
            if char.isdigit():
                
                num.append(char)
            
            elif char == '[':
                
                stack.append('')
                number = int(''.join(num))
                nums.append(number)
                num = []
            
            elif char == ']':
                
                x = stack.pop()*nums.pop()
                stack[-1] += x
            
            else:
                
                stack[-1] += char
        
        return stack[0]

a = Solution()
b = a.decodeString('4[abc]5[df]')