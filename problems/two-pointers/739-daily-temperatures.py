"""
Link: https://leetcode.com/problems/daily-temperatures
Difficulty: medium

Problem:
return a list that corresponds to number of days till next highest temp

Input / Output:


Notes:


Solution Approaches:
2x dp
    1 memo for temps
    1 memo for days

Iterate backwards in orginal tempratures list
see if prev temp
    1. imperically larger - if so then res[i] = delta in days
    2. fallback to the dp of temps to see if dp has a larger day -- if so then res[j]+delta

"""
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0]*len(temperatures)
        dp = [0]*len(temperatures)
        temperatures = temperatures[::-1]
        curr_max = temperatures[0]
        dp[0] = temperatures[0]
        for i,v in enumerate(temperatures):
            if i==0: res[0]=0
            elif v>=curr_max:
                curr_max = v
                res[i] = 0
                dp[i] = v
            else:
                j = i
                while j>=0:
                    if temperatures[j] > v:
                        res[i] = i-j
                        dp[i] = temperatures[j]
                        break
                    elif dp[j]>v:
                        res[i] = res[j]+(i-j)
                        dp[i] = dp[j]
                        break
                    j-=1
        return res[::-1]