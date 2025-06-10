"""
Link: https://leetcode.com/problems/subsets-ii
Difficulty: medium

Problem:
Create subset with pool including duplicate nums.
Result should *not* have duplicates.

Input / Output:


Notes:


Solution Approaches:
Backtrack. Seed in sorted pool. 

"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if not nums: return res
        queue = [([], sorted(nums))]
        while queue:
            curr, pool = queue.pop(0)
            res.append(curr)
            if pool:
                for i,v in enumerate(pool):
                    if i>0 and pool[i-1]==v:
                        continue
                    queue.append((curr+[v], pool[i+1:]))
        return res