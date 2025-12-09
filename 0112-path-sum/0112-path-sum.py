class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        # If it's a leaf, check if the sum matches
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recursive check for left or right subtree
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))
