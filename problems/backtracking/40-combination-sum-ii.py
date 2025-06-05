"""
Link: https://leetcode.com/problems/combination-sum-ii
Difficulty: meidum

Problem:


Input / Output:


Notes:


Solution Approaches:
Solution Approaches:
1. seed *sorted* pool / empty list
2. backtrack build up each
    - skip if previous in pool equal (how to avoid dups)

"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if not candidates: return res
        queue = [([], 0, sorted(candidates))]
        while queue:
            curr_comb, curr_sum, pool = queue.pop(0)
            for i,v in enumerate(pool):
                temp = curr_sum + v
                temp_comb = curr_comb+[v]
                if i>0 and v == pool[i-1]:
                    continue
                elif temp == target:
                    res.append(temp_comb)
                elif target > temp:
                    temp_pool = pool[i+1:]
                    queue.append((temp_comb, temp, temp_pool))
        return res
        