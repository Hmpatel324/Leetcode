"""
Link: https://leetcode.com/problems/relative-ranks
Difficulty: easy

Problem:
transform score of people into relative ranks in a competition

Input / Output:


Notes:


Solution Approaches:
Sort in reverse order
Convert to a dictionary value: sort index
Map original to dictionary value

"""
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        hp = {}
        for i,v in enumerate(sorted(score, reverse=True)):
            if i == 0:
                hp[v] = "Gold Medal"
            elif i==1:
                hp[v] = "Silver Medal"
            elif i==2:
                hp[v] = "Bronze Medal"
            else: 
                hp[v] = str(i+1)
        return list(map(lambda x: hp[x], score))