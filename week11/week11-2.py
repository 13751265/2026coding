# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a=[] #放答案
        def helper(root):
            count=0 #問下便幾個p,q的node
            if root==None:return 0 #沒有東西
            if root==p or root==q:count+=1 #找到一個
            count +=helper(root.left)
            count +=helper(root.right)
            if count==2:  #收集齊2個
                a.append(root) #要記下答案
            return count #收集到幾個
        helper(root) #函式呼叫函式
        return a[0] #最前面,第一次出現的答案
