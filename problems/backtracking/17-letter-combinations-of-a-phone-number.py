"""
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number
Difficulty: med

Problem:
build the alias of a phone number from the number itself

Input / Output:


Notes:


Solution Approaches:
combination problem - build up

"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        if not digits: return res
        cache = {"2":["a","b","c"], "3":["d","e","f"], "4" :["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"]}
        queue = [("",digits)]
        while queue:
            curr, pool = queue.pop(0)
            if not pool: res.append(curr)
            else:
                new_pool = pool[1:]
                for letter in cache[pool[0]]:
                    queue.append((curr+letter, new_pool))
        return res