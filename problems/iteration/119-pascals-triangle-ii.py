"""
Link: https://leetcode.com/problems/pascals-triangle-ii
Difficulty: easy

Problem:
return the pascal triangles row

Input / Output:


Notes:


Solution Approaches:
0 == [1]
then for all subsequent: [1] + [created via 2p] + [1]

"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0: return [1]
        queue = (0,[])
        while queue:
            curr_ri, curr_row = queue
            if curr_ri == rowIndex: return curr_row
            temp = []
            slow, fast = 0, 1
            while fast <= len(curr_row)-1:
                temp.append(curr_row[slow]+curr_row[fast])
                slow+=1
                fast+=1
            temp = [1] + temp + [1]
            queue = (curr_ri+1, temp)


        