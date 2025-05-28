"""
Link: https://leetcode.com/problems/find-the-town-judge
Difficulty: easy

Problem:
Determine if there exists a Town Judge - everyone trusts judge but judge trusts no one else

Input / Output:


Notes:


Solution Approaches:
Double graph to track in and out degrees

"""
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        graph = [[0,0] for j in range(n)]
        for edge in trust:
            graph[edge[0]-1][1]+=1
            graph[edge[1]-1][0]+=1

        for i,v in enumerate(graph):
            if v[0]==n-1 and v[1]==0:
                return i+1
        return -1