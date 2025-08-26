"""
Link: https://leetcode.com/problems/k-closest-points-to-origin
Difficulty: medium

Problem:
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
 return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Input / Output:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]

Notes:


Solution Approaches:
use a minheap to track/evict when it goes over

"""
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        heap = []
        heapq.heapify(heap)

        for point in points:
            euc = -1*((point[0]**2 + point[1]**2)**.5)
            heapq.heappush(heap,(euc,point))
            if len(heap)>k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            euc,point = heapq.heappop(heap)
            res.append(point)
        return res