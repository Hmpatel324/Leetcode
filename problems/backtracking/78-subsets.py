"""
Link: https://leetcode.com/problems/subsets
Difficulty: medium

Problem:
Create a power set - all combos of a list of numbers

Input / Output:


Notes:


Solution Approaches:
Backtrack basic
    - avoids dups by only passing passing pool[i+1:] to next invokation

"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        queue = [([], nums)]
        while queue:
            curr, pool = queue.pop(0)
            res.append(curr)
            for i,v in enumerate(pool):
                queue.append((curr+[v], pool[i+1:]))
        return res