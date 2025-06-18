"""
Link: https://leetcode.com/problems/combinations
Difficulty: medium

Problem:
Generate all combinations of given length K

Input / Output:


Notes:


Solution Approaches:
BAcktrack build up
Seed in ([], list(range(1,n+1)))
build up each

"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        queue = [([], list(range(1,n+1)))]
        while queue:
            curr, pool = queue.pop()
            for i,v in enumerate(pool):
                temp = curr + [v]
                if len(temp)==k: res.append(temp)
                else: queue.append((temp, pool[i+1:]))
        return res