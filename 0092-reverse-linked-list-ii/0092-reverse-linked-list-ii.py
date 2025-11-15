class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        # Step 1: Move prev to the node before 'left'
        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next

        # Step 2: Reverse sublist using head insertion
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
