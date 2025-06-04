"""
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
Difficulty: medium  

Problem:
Find lowest common ancestor of two nodes

Input / Output:


Notes:


Solution Approaches:
The key is this is a BST therefore want to find the node that is in between high/low or is itself one of the nodes
Iteratively BFS down the tree and find a node that fits a return condition

"""
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        queue = [root]
        low,high = min(p.val,q.val),max(p.val,q.val)
        while(queue):
            curr = queue.pop()
            if(curr.val>low and curr.val<high):
                return curr
            elif(curr==p or curr==q):
                return curr
            else:
                if(low<curr.val):
                    queue.append(curr.left)
                else:
                    queue.append(curr.right)