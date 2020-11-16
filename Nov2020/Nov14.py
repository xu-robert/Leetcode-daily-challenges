# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 23:24:31 2020
Poor pigs

subset problem.

Think about the problem this way instead: with n pigs and x rounds to test, (x being minutes to test/minutes to die), whats the max
number of buckets we can test so we can be sure we know exactly which bucket contains the poison?

Base case with 1 round: Example, how many buckets can we predict with 2 pigs in one round?

Ans: We can resolve max 4 buckets with 2 pigs. (2**2) - The possible pig deaths are (P1), (P2), (P1,P2), (). 
Bucket 1 fed to pig 1 only, 2 to pig 2 only, 3 to pig 1 and pig 2, and no pig feeds from bucket 4. We know that one of the four possible
pig deaths will occur, each corresponding to a single bucket (if p1 and p2 die, since only bucket 3 fed them both, we know its bucket 3).

We can also express this like the following (1,0),(0,0),(0,1),(1,1), where the first element indicates which round pig 1 died, and the
second element indicates the round that pig 2 died. With one round, there is a binary choice

Similarly, with 3 pigs, 1 round, there are 8 possible pig deaths (2**3) with 8 possible death scenarios. (1,0,0), (0,1,0), (0,0,1)
(1,1,0), (1,1,1), (0,1,1), (0,0,0), (1, 0, 1)

Generalize this to one round: With one round and n pigs, at most 2**n buckets can be tested.

General case: x rounds instead of just 1.

Notice how with just 1 round, there are 2 choices for each pig: it can either die in round 1 or it does not die. This is why we have
2**n buckets. With 2 rounds, there are 3 choices for each pig now: it can die in round 1, die in round 2, or not die. With this insight 
it sounds like we could estimate 3**n buckets. For 2 pigs, the possible choice set is (0,0),(1,0),(0,1),(1,1),(1,2),(2,1),(0,2),(2,0),(2,2).
In fact, we can guarantee that only one of the choices from that set will be the result of two rounds through how we distribute buckets
to pigs. (0,0) is the result if neither pig drinks from that particular bucket in both rounds. (1,0) is the result if pig 1 drinks from
that bucket in round 1 and no pig drinks from that bucket in round 2. As it turns out, we can generalize this result to x buckets. With
n pigs and x rounds, we can figure out the poison bucket from (x+1)**n buckets.

Since the question asks for the minimum number of pigs, we just increment number of pigs starting from 1 until we exceed num of buckets,
at this point n is the smallest number of pigs. Special case if buckets is 1: since we know one of the buckets is poisoned, if there is 
only one bucket, it must be poisoned and we don't need to use any pigs.'

@author: Robert Xu
"""
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        
        if buckets == 1: return 0
        
        n = (minutesToTest/minutesToDie)+1
        
        i = 1
        num = n**1
        
        while num < buckets:
            i += 1
            num = n**i
        
        return i
            