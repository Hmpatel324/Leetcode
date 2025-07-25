"""
Link: https://leetcode.com/problems/defuse-the-bomb
Difficulty: easy

Problem:
To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

Input / Output:
Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]

Notes:


Solution Approaches:
2p + sliding window to move the mapped value

"""
class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = [0]*len(code)
        if k==0: return res
        
        i=0
        window = sum(code[1:k+1]) if k>0 else sum(code[k:])
        l,h = (1,k) if k>0 else (k,-1)

        while i<len(code):
            res[i] = window
            window-=code[l]
            l+=1
            h+=1
            if h==len(code): h=0
            if l==len(code): l = 0
            window += code[h]
            i+=1
        return res
