"""
Link: https://leetcode.com/problems/keys-and-rooms
Difficulty: medium

Problem:
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

Input / Output:
Input: rooms = [[1],[2],[3],[]]
Output: true

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
cannot get to room two

Notes:


Solution Approaches:
Breadth First Exploration variation

"""
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        queue = [0]
        visited.add(0)
        while queue:
            curr_room = queue.pop(0)
            for key in rooms[curr_room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
        return len(visited)==len(rooms)