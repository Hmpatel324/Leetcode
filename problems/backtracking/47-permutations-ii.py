"""
Link: https://leetcode.com/problems/permutations-ii
Difficulty: med

Problem:
Return unique permutations 

Input / Output:


Notes:


Solution Approaches:
1. seed *sorted* pool / empty list
2. backtrack build up each
    - skip if previous in pool equal (how to avoid dups)

"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if not nums: return res
        queue = [([], sorted(nums))]
        while queue:
            curr_perm, pool = queue.pop()
            for i,v in enumerate(pool):
                if i > 0 and pool[i-1]== v:
                    continue
                temp_perm = curr_perm + [v]
                temp_pool = pool[:i] + pool[i+1:]
                if not temp_pool:
                    res.append(temp_perm)
                else:
                    queue.append((temp_perm, temp_pool))
        return res