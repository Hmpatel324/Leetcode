"""
Link: https://leetcode.com/problems/network-delay-time
Difficulty: medium

Problem:
You are given a network of n nodes, labeled from 1 to n. 
You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. 
If it is impossible for all the n nodes to receive the signal, return -1.

Input / Output:
times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
output: 2

Notes:


Solution Approaches:
Djikstra Algorithm

"""
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # Setup
        cache = {i:float('inf') for i in range(1,n+1)}
        cache[0] = 0

        # convert times into a graph
        graph = defaultdict(list)
        for edge in times:
            graph[edge[0]].append((edge[1],edge[2]))
        
        # Breadth first exploration
        heap = [(k,0)]
        cache[k] = 0

        while heap:
            curr_node, curr_path_time = heappop(heap)
            for n,w in graph[curr_node]:
                temp = w+curr_path_time
                if temp<cache[n]:
                    cache[n] = temp
                    heappush(heap,(n,temp))

        res = 0
        res = max(cache.values())
        return -1 if res ==float('inf') else res 
