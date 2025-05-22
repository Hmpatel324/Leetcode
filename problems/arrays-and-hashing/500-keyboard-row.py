"""
Link: https://leetcode.com/problems/keyboard-row
Difficulty: easy

Problem:
Given list of words, determine which words can be created from keyboard rows

Input / Output:


Notes:


Solution Approaches:
pre-process each kb row into a cache set pool then run through each word

"""
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        res = []
        r1 = set("qwertyuiop")
        r2 = set("asdfghjkl")
        r3 = set("zxcvbnm")

        for word in words:
            temp = word.lower()
            pool = r1 if temp[0] in r1 else r2 if temp[0] in r2 else r3
            add_word = True
            for letter in set(temp):
                if letter not in pool:
                    add_word = False
                    break
            if add_word: res.append(word)
        return res