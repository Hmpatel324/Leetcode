"""
Link: https://leetcode.com/problems/last-stone-weight
Difficulty: easy

Problem:
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

Input / Output:
Input: stones = [2,7,4,1,8,1]
Output: 1

Notes:


Solution Approaches:

"""
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = [-i for i in stones]
        heapq.heapify(heap)

        while len(heap)>1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)

            if x!=y:
                heapq.heappush(heap,y-x)
        
        return 0 if not heap else -1*heap[0]