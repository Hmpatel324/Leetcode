"""
Link: https://leetcode.com/problems/loud-and-rich
Difficulty: medium

Problem:
There is a group of n people labeled from 0 to n - 1 where each person has a different amount of money and a different level of quietness.

You are given an array richer where richer[i] = [ai, bi] indicates that ai has more money than bi and an integer array quiet where quiet[i] is the quietness of the ith person. 
All the given data in richer are logically correct (i.e., the data will not lead you to a situation where x is richer than y and y is richer than x at the same time).

Return an integer array answer where answer[x] = y if y is the least quiet person (that is, the person y with the smallest value of quiet[y]) 
among all people who definitely have equal to or more money than the person x.

Input / Output:


Notes:


Solution Approaches:
Breadth first build for richer neighbors as associative property in effect
Then for do determine quitest

"""
class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        people = len(quiet)
        richer_graph = defaultdict(list)
        
        for edge in richer:
            richer_graph[edge[1]].append(edge[0])

        def get_richer_neighbors(person):
            res = set()
            queue = [person]
            while queue:
                curr = queue.pop()
                res.add(curr)
                for n in richer_graph[curr]:
                    if n not in res: queue.append(n)
            return res


        ans = [0]*people
        for i in range(people):
            richer_neighbors = get_richer_neighbors(i)
            quietest_neighbor = float('inf')
            for neighbor in richer_neighbors:
                if quiet[neighbor] < quietest_neighbor:
                    quietest_neighbor = quiet[neighbor]
                    ans[i] = neighbor
        return ans