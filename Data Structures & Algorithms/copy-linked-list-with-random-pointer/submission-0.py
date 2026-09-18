class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Map: original node → copied node
        mapping = {}

        # First pass: create all copied nodes
        current = head
        while current:
            mapping[current] = Node(current.val)
            current = current.next

        # Second pass: connect next and random
        current = head
        while current:
            mapping[current].next = mapping.get(current.next)
            mapping[current].random = mapping.get(current.random)

            current = current.next

        return mapping[head]