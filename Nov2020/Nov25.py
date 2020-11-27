# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:37:48 2020

The solution relies on the distributive property of the modulo operation.

Based on the hint given, we know that 1111 = 111*10 + 1, and we are trying to find a number such that
111..111 % k == 0. We need to use the remainder rather than the actual n, because it may overflow. 

Take for example k = 33. We begin by evaluating n = 11 to see if it will give the correct answer

11% 33 = 11 != 0: therefore we need to keep iterating. 

Next we try 111 (but in reality we only keep track of the number of digits, digs)

We need to use modular arithmetic now to address the question in terms of remainders.

Keep in mind two properties:
    
(a + b) % c = (a%c + b%c) % c (additive distributive)
(ab)%c = ((a%c)*(b%c)) % c (multiplicative distributive)

Write 11 = k*x + R where x is the largest integer such that k*x <= n and R is thus N%K

In this case, 11 = 33*0 + 11%33

Then for 111:
    
111 = 10*11 + 1
111 % 33 = (10*11 + 1) % 33 = (10 * (33*0 + 11%33) + 1) % 33
the RHS:
(10*33*0 + 10*11%33 + 1) % 33
by additive:
(10*33*0%33 + (10*11%33)%33 + 1%33)%33
the first term cancels to zero (regardless of what x is, because (10*k*x)%k is always 0)
thus we have
((10*11%33)%33 + 1%33)%33
applying additive again
(10*11%33 + 1)%33

where 11%33 = R

(10R+1)%K

In general: (10N + 1) % K = (10R + 1) % K, where R is N%K

So we keep incrementing N until R reaches 0, exclusing the cases where K%2 == 0 or k%5 == 0, as you can
see multiples of these numbers never end in 1. 


@author: Robert Xu
"""
class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K % 2 == 0: return -1
        if K % 5 == 0: return -1
        
        temp = str(K)
        n = int('1'*(len(temp)))
        digs = len(temp)
        rem = n % K
        
        while rem != 0:
            rem = (rem*10 + 1) % K
            digs += 1
        
        return digs

a = Solution()
b = a.smallestRepunitDivByK(3)
        
        
                