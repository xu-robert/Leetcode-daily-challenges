# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 09:20:47 2020
Longest Substring with At Least K Repeating Characters


Given a string s and an integer k, return the length of the longest substring of s such that the 
frequency of each character in this substring is greater than or equal to k.

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5


Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

Actually this is quite a hard question. This is not my original solution, which did not perform very
well, but this one runs in O(26N) time which is really good. I couldn not come up with this myself.This
solution transforms the question slightly.

The central idea is sliding window, where we try to figure out the max length of a substring which contains
n unique elements that each appear no less than k times in the substring. The key is that in the
original question, we don't know what n is, but we do know that it is bounded between 
1 and 26 since the string contains lowercase letters only. By trying n from 1 to 26, 
we definitely will arrive at the optimal solution.

Keep a frequency dictionary to track number of occurences of characters in a substring
keep a variable ans to retain the max length of substring with n unique characters appearing >= k time
variable n_unique, the number of unique characters in the substring
variable n_no_less_than_k, the number of unique characters in substring which occur at least k times 
in the substring

Rules for expanding and contracting the window given that we need to find n unique elements in a window:

Each time we reach the next element, increment its count. If its count == 1, then this is the first time
we have seen it in the substring so increment n_unique. If its frequency == k, then increment n_no_less_than_k.
Only do this when equal to k. 

If n_unique > n, we need to decrease the window since we have too many unique elements in the window.
Works backwards from the increasing rules. We decrement the count of the element at the lower bound. If
its count == 0, decrease n_unique. If count == k-1, then it no longer appears at least k times so
we decrement n_no_less_than_k variable. Again, only do this once per element. Repeat until n_unique == n.

Finally, if n_unique == n_no_less_than_k, this means the every unique element in the substring occurs
at least k times, so we update ans for this value of n. Repeat through the whole string, then continue
to next n.

@author: Robert Xu
"""

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        def longest_substring_with_n_unique(n, s, k):
            
            ans = 0
            i = 0
            freqs = {c: 0 for c in set(s)}
            n_unique = 0
            n_no_less_than_k = 0
            
            for j in range(len(s)):
                
                freqs[s[j]] += 1
                if freqs[s[j]] == k: n_no_less_than_k += 1
                if freqs[s[j]] == 1: n_unique += 1
                
                while n_unique > n:
                    freqs[s[i]] -= 1
                    if freqs[s[i]] == 0:
                        n_unique -= 1
                    if freqs[s[i]] == k-1:
                        n_no_less_than_k -= 1
                    i += 1
                
                if n_unique == n and n_no_less_than_k == n:
                    ans = max(ans, j-i+1)
            
            return ans
                
        ans = 0
        
        for n in range(1, 27):
            
            ans = max(ans, longest_substring_with_n_unique(n, s, k))
        
        return ans
        
