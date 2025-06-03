"""
Link: https://leetcode.com/problems/permutations
Difficulty: medium

Problem:
Given nums array - return all permutations of it

Input / Output:


Notes:


Solution Approaches:
Backtrack build up via iterative queue 
Seed empty list with all nums into queue
and build up

"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if not nums: return res
        queue = [([], nums)]
        while queue:
            curr_perm, curr_pool = queue.pop(0)
            for i,v in enumerate(curr_pool):
                new_perm = curr_perm + [v]
                new_pool = curr_pool[:i] + curr_pool[i+1:]
                if not new_pool:
                    res.append(new_perm)
                else:
                    queue.append((new_perm, new_pool))
        return res