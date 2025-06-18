"""
Link: https://leetcode.com/problems/word-search
Difficulty: medium

Problem:
Determine True or False if a word exists in a word search

Input / Output:


Notes:


Solution Approaches:
Graph based search
Have a explore helper function

"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        r_max, c_max = len(board), len(board[0])
        def helper(r_in, c_in):
            queue = [(r_in, c_in, set(), word)]
            while queue:
                r, c, visited, curr = queue.pop()
                temp = curr[1:]
                if not temp: return True
                temp_visited = visited | {(r,c)}
                for r_n, c_n in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if 0<=r_n<r_max and 0<=c_n<c_max and (r_n,c_n) not in temp_visited and board[r_n][c_n]==temp[0]:
                        queue.append((r_n,c_n,temp_visited,temp))
            return False
        
        for i in range(r_max):
            for j in range(c_max):
                if board[i][j]==word[0]:
                    res = helper(i,j)
                    if res: return True
        return False