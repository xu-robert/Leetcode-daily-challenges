# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 10:00:51 2020
Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5

SOlution

All of these calculating expression type questions are solvable with a stack. The challenge is making the code concise
There are a few key concpets here: The top of stack is the most recently seen number. As we loop through
the string, we take care of multiplication and division as soon as we encounter it, and addition and subtraction
at the end. Every time we hit an operator, we know that the number on top of the stack is complete. 
We want to know what the last operator was, since that will be the one that affects the number on top of the stack.
If the last operator is '+', then we leave the number as. We will take care of it in the final step, since addition
comes after multiplication and division. If the last operator is '-', then we flip the sign of the top number of 
the stack. This is so in the last step, we are subtracting this number from everything else. If last operator is 
'*', the top stack element is multiplied by the second top element, and similarly if the operator is '/'. The cast to
int ensures that the number is rounded towards 0. Each time we encounter an operator, we store it as 'last' and begin
a new number on the top of the stack. Once all the * and / are taken care of, we can just sum the whole steack.

Other note: we append a special symbol to the end of the string so we know to carry out an operation with the last 
number on top of the stack. The solution can also be shortened by moving the append statements outside the individual
elif loops since we do it everytime we encounter a new operator. This means we can also remove the if last == '+' 

Final note: there is a way to do this in O(n) time and O(1) space, but I havent looked into it.

statement.
@author: Robert Xu
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += '$'
        stack = [0]
        last = '+'
        for c in s:
            
            if c.isdigit():
                stack[-1] = stack[-1]*10 + int(c)
            
            elif c in "+-*/$":
                if last == '+':
                    stack.append(0)
                elif last == '-':
                    stack[-1] *= -1
                    stack.append(0)
                elif last == '*':
                    x = stack.pop()
                    stack[-1] *= x
                    stack.append(0)
                elif last == '/':
                    x = stack.pop()
                    stack[-1] = int(stack[-1]/x)
                    stack.append(0)
                last = c
            
        return sum(stack)

a = Solution()
b = a.calculate("14 - 3/2")
                
            
                
                