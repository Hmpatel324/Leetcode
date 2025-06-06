"""
Link: https://leetcode.com/problems/3sum/
Difficulty: med

Problem:
find 3 ints in the list that add to 0

Input / Output:


Notes:


Solution Approaches:
Backtrack candidate creation and check
To avoid duplicate entries, a sorted candidate int list must be seeded

"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if not nums: return res
        queue = [([], sorted(nums))]
        while queue:
            curr_comb, pool = queue.pop(0)
            for i,v in enumerate(pool):
                temp_comb = curr_comb+[v]
                if i>0 and pool[i-1] == v:
                    continue
                elif len(temp_comb)==3 and sum(temp_comb)==0:
                    res.append(temp_comb)
                elif len(temp_comb)<3: 
                    queue.append((temp_comb, pool[i+1:]))
        return res