"""
Link: https://leetcode.com/problems/flood-fill
Difficulty: easy

Problem:
Given seed cell, fill in all adjacent cells that match original cell color


Input / Output:


Notes:


Solution Approaches:
iterative approach. Use a queue to add and use a set to track already processed.

"""
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        visited = set()
        original_color = image[sr][sc]
        queue = [(sr,sc)]
        while queue:
            curr_r, curr_c = queue.pop(0)
            if (curr_r, curr_c) not in visited:
                visited.add((curr_r,curr_c))
                image[curr_r][curr_c]=color
                for n_r, n_c in [(curr_r+1, curr_c), (curr_r-1, curr_c), (curr_r,curr_c+1), (curr_r, curr_c-1)]:
                    if 0 <= n_r <= len(image)-1 and 0 <= n_c <= len(image[0])-1 and (n_r,n_c) not in visited and image[n_r][n_c]==original_color:
                        queue.append((n_r,n_c))
        return image
