"""
Link: https://leetcode.com/problems/combination-sum
Difficulty: medium

Problem:
Given a candidate pool and target, determine the combinations that from candidates that sum to target

Input / Output:


Notes:


Solution Approaches:
Backtracking / pool creation
Seed a tuple with empty, 0 sum, all candidates and iteratively buildup

"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if not candidates: return res
        queue = [([], 0, candidates)]
        while queue:
            curr_comb, curr_sum, pool = queue.pop(0)
            for i,v in enumerate(pool):
                temp = curr_sum + v
                temp_comb = curr_comb+[v]
                if temp == target:
                    res.append(temp_comb)
                elif target > temp:
                    queue.append((temp_comb, temp, pool[i:]))
        return res