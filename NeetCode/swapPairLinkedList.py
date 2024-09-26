
def swapPairs(self, A):

    # Dummy node
    head = ListNode(0)
    # Point the next of dummy node to the head
    head.next = A
    # This node will be used to traverse the list
    current = head
    # Loop until we reach to the second last node
    while current.next and current.next.next:
        # First node of the pair
        first = current.next
        # Second node of the pair
        second = current.next.next
        # Point the next of first node to the node after second node
        first.next = second.next
        # Now the current node's next should be the second node
        current.next = second
        # Linking the original second node to the first node
        current.next.next = first
        # Move the pointer two nodes ahead
        current = current.next.next
    return head.next



def swap_pairs1(n):
  if n and n.next:
    head = n.next
    head.next, n.next = n, swap_pairs(head.next)
    return head
  return n
# this will have issue of size of recurring stack (say 999)