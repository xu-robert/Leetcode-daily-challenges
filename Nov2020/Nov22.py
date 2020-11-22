# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 08:58:02 2020
Unique Morse Code Words

Just use set to store unique words

@author: Robert Xu
"""
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        ans = set()
        
        for word in words:
            
            word_code = ''
            
            for letter in word:
                
                word_code += code[ord(letter)-ord('a')]
            
            ans.add(word_code)
        
        return len(ans)
    
a = Solution()
b = a.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])