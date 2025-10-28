# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head

        # Step 1: find length
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: make it circular
        tail.next = head

        # Step 3: find new tail (n - k % n - 1)
        k = k % length
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        # Step 4: break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head
