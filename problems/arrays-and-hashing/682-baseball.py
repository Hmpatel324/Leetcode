"""
Link: https://leetcode.com/problems/baseball-game
Difficulty: easy

Problem:
Decode baseball operations into a score

Input / Output:


Notes:


Solution Approaches:
for loop using a list as a stack

"""
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = []
        for op in operations:
            if op == "+":
                res.append(res[-1]+res[-2])
            elif op == "D":
                res.append(2*res[-1])
            elif op == "C":
                res.pop()
            else:
                res.append(int(op))
        return reduce(lambda x, y:x+y, res) if res else 0