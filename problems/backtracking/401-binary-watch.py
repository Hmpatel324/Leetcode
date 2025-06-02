"""
Link: https://leetcode.com/problems/binary-watch
Difficulty: easy

Problem:
convert a binary watch output to all possible time combinations given number of lights on

Input / Output:


Notes:


Solution Approaches:
Backtracking buildup

"""
class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        if turnedOn == 0: return ["0:00"]
        candidates = [(8,0), (4,0), (2,0), (1,0), (0,32), (0,16), (0,8), (0,4), (0,2), (0,1)]
        res = []
        queue = [((0,0), 0, candidates)]
        while queue:
            curr_time, curr_on, pool = queue.pop(0)
            if curr_on < turnedOn:
                for i,v in enumerate(pool):
                    new_on = curr_on+1
                    curr_hour, curr_min = curr_time 
                    pool_hour, pool_mins = v
                    new_hour = curr_hour + pool_hour
                    new_min = curr_min+pool_mins
                    new_pool = pool[i+1:]
                    if new_on == turnedOn:
                        if (new_hour<=11 and new_min<=59):
                            str_hour = str(new_hour)
                            str_mins = str(new_min) if new_min > 9 else "0"+str(new_min)
                            res.append(str_hour+":"+str_mins)
                    elif new_on < turnedOn:
                        queue.append(((new_hour, new_min), new_on, new_pool))
        return res