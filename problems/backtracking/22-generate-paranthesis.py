"""
Link: https://leetcode.com/problems/generate-parentheses/
Difficulty: medium

Problem:
Given a int, generate all potential parenthesis combinations

Input / Output:


Notes:


Solution Approaches:
Seed in empty string, 0 opened, 0 closed and use backtracking to build up combinations

"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        if n==0: return res
        queue = [("",0,0)]
        while queue:
            curr, curr_open, curr_closed = queue.pop(0)
            if curr_open==curr_closed==n: res.append(curr)
            if curr_open<n: queue.append((curr+"(",curr_open+1,curr_closed))
            if curr_closed<curr_open: queue.append((curr+")", curr_open, curr_closed+1))
        return res