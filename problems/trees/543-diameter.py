"""
Link: https://leetcode.com/problems/diameter-of-binary-tree
Difficulty: easy

Problem:
provide tree diameter

Input / Output:


Notes:


Solution Approaches:
Post order traversal + extra computation of 1+ on way back up

"""
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = 0
        if not root: return res
        stack = [root]
        visited = {}
        while(stack):
            curr = stack.pop()
            if not curr in visited:
                visited[curr] = 0
                stack.append(curr)
                if curr.left: 
                    stack.append(curr.left)
                if curr.right: 
                    stack.append(curr.right)
            else:
                left = (1 + visited[curr.right] if curr.right else 0)
                right = (1 + visited[curr.left] if curr.left else 0)
                curr_diamater = left + right 
                res = max(res, curr_diamater)
                visited[curr] = max(left,right)

        return res