"""
Link: https://leetcode.com/problems/pascals-triangle
Difficulty: easy

Problem:
print out pascals triangle given the input of the height lvl

Input / Output:
5 => [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Notes:


Solution Approaches:
iteration / seeding

"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        if numRows == 1: return res
        current_level = 1
        queue = []
        while current_level < numRows:
            new_level = []
            new_level.append(1)
            i = 0
            while i <= len(queue)-2:
                new_level.append(queue[i] + queue[i+1])
                i += 1
            new_level.append(1)
            res.append(new_level)
            queue = new_level
            current_level += 1
        return res