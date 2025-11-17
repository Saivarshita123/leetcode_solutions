class Solution(object):
    def generateTrees(self, n):
        if n == 0:
            return []

        # Function to generate all trees for values from start to end
        def build(start, end):
            if start > end:
                return [None]   # empty tree

            results = []

            # choose root
            for root_val in range(start, end + 1):
                
                left_trees = build(start, root_val - 1)   # all possible left subtrees
                right_trees = build(root_val + 1, end)    # all possible right subtrees

                # combine each left with each right
                for L in left_trees:
                    for R in right_trees:
                        root = TreeNode(root_val)
                        root.left = L
                        root.right = R
                        results.append(root)

            return results

        return build(1, n)