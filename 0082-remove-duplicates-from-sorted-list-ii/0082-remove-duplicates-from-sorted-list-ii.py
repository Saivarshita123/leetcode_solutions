# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            # If current node has duplicates
            if curr.next and curr.val == curr.next.val:
                # Skip all nodes with same value
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next  # remove all duplicates
            else:
                prev = prev.next  # move prev if no duplicates
            curr = curr.next

        return dummy.next
