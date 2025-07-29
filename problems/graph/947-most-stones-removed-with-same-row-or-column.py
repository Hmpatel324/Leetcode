"""
Link: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column
Difficulty: medium

Problem:
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.
A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.
Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

Input / Output:
[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
5

Notes:


Solution Approaches:
Modified union find algorithm
Basically want to determine the number of unions

"""
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        graph_row = defaultdict(list)
        graph_col = defaultdict(list)
        for stone in stones:
            graph_row[stone[0]].append(stone[1])
            graph_col[stone[1]].append(stone[0])

        observed = set()
        def findUnionSize(stone_r,stone_c):
            union_size = 0
            queue = [(stone_r,stone_c)]
            while queue:
                r,c = queue.pop(0)
                union_size += 1
                for n_c in graph_row[r]:
                    if (r,n_c) not in observed:
                        observed.add((r,n_c))
                        queue.append((r,n_c))
                for n_r in graph_col[c]:
                    if (n_r,c) not in observed:
                        observed.add((n_r,c))
                        queue.append((n_r,c))
            return union_size
         
        res = 0
        for s in stones:
            r,c = s[0],s[1]
            if (r,c) not in observed:
                observed.add((r,c))
                u_s = findUnionSize(r,c)
                res += (u_s-1)
        return res