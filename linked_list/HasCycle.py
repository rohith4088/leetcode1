class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def HasCycle(head):
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Function to create a linked list with a cycle for testing
def create_linked_list_with_cycle(values, cycle_position):
    nodes = [Node(value) for value in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    # Create the cycle
    nodes[-1].next = nodes[cycle_position]
    return nodes[0]

# Example usage
if __name__ == "__main__":
    # Create a linked list with a cycle at position 2 (0-indexed)
    head = create_linked_list_with_cycle([1, 2, 3, 4, 5], 2)
    print(HasCycle(head))  # Should print True

    # Create a linked list without a cycle
    head = create_linked_list_with_cycle([1, 2, 3, 4, 5], -1)
    print(HasCycle(head))  # Should print False
