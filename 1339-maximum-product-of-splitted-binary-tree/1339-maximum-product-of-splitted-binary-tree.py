class Solution:
    def maxProduct(self, root):
        MOD = 10**9 + 7
        self.max_product = 0

        # First DFS to compute total sum
        def total_sum(node):
            if not node:
                return 0
            return node.val + total_sum(node.left) + total_sum(node.right)

        total = total_sum(root)

        # Second DFS to compute subtree sums and products
        def subtree_sum(node):
            if not node:
                return 0
            left = subtree_sum(node.left)
            right = subtree_sum(node.right)
            curr_sum = node.val + left + right

            # Try splitting here
            self.max_product = max(
                self.max_product,
                curr_sum * (total - curr_sum)
            )

            return curr_sum

        subtree_sum(root)
        return self.max_product % MOD
