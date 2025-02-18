class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detect_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


nodes = [ListNode(i) for i in range(1, 10)]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]
#nodes[8].next = nodes[2]

has_cycle = detect_cycle(nodes[0])
print(f"Cycle detected: {has_cycle}")
