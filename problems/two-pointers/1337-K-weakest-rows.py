"""
Link: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix
Difficulty: easy

Problem:
Find k "weakest" rows based on 1/0s

Input / Output:


Notes:


Solution Approaches:
Modified Binary search

"""
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        cache = collections.defaultdict(list)
        for i in range(len(mat)):
            lo, hi = 0, len(mat[i])-1
            while lo<=hi:
                mid = lo + ((hi-lo)/2)
                mid_value = mat[i][mid]
                if mid_value==0 and (mid==0 or mat[i][mid-1]==1):
                    cache[mid].append(i)
                    break
                elif mid_value==1:
                    lo = mid+1
                else:
                    hi = mid-1
            if lo>hi: cache[len(mat[i])].append(i)
        
        res = []
        for i in sorted(cache.keys()):
            res+=cache[i]
            if len(res)>=k:
                break
        return res[:k]