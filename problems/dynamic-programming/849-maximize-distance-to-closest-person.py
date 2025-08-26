"""
Link: https://leetcode.com/problems/maximize-distance-to-closest-person
Difficulty: medium

Problem:
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, 
and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.

Input / Output:
Input: seats = [1,0,0,0,1,0,1]
Output: 2

Input: seats = [1,0,0,0]
Output: 3

Notes:


Solution Approaches:
2 dps
fwd run
rev run
then consolidate

"""
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        
        dp_fwd = [0]*len(seats)
        dp_rev = [0]*len(seats)

        # Fwd
        for i,v in enumerate(seats):
            if i == 0:
                dp_fwd[i] = float('inf') if v==0 else 0
            elif v==1:
                dp_fwd[i] = 0
            # open
            else:
                dp_fwd[i] = dp_fwd[i-1]+1
        
        # Backward
        for i,v in reversed(list(enumerate(seats))):
            if i==len(seats)-1:
                dp_rev[i] = float('inf') if v==0 else 0
            # seat occupied
            elif v==1:
                dp_rev[i] = 0
            # open
            else:
                dp_rev[i] = dp_rev[i+1]+1
        
        res = 1
        # consolidate
        for i in range(0,len(seats)):
            res = max(res, min(dp_fwd[i],dp_rev[i]))
        
        return res