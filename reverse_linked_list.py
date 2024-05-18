class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # @param A : head node of linked list
    # @param B : integer (start position)
    # @param C : integer (end position)
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        if not A or B == C:
            return A

        # Create a dummy node to simplify the edge cases
        dummy = ListNode(0)
        dummy.next = A
        pre = dummy

        # Move `pre` to the node just before the reversal segment
        for _ in range(B - 1):
            pre = pre.next

        # `start` is the first node to be reversed
        start = pre.next
        # `then` is the node that will be moved during the reversal
        then = start.next

        # Reverse the segment between B and C
        for _ in range(C - B):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next

        return dummy.next


# Helper function to print the list (for testing purposes)
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("NULL")


# Example usage
# Constructing the linked list 1 -> 2 -> 3 -> 4 -> 5 -> NULL
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
new_head = sol.reverseBetween(head, 2, 4)

# Printing the modified list
print_list(new_head)  # Expected output: 1 -> 4 -> 3 -> 2 -> 5 -> NULL
