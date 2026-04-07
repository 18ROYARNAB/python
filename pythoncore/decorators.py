class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    # display
    def display(self):
        if self.head is None:
            print("empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.data)
                curr = curr.next

    # input sll using append
    def append(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
        else:
            curr = self.head
            # FIX: Stop AT the last node, not after it
            while curr.next is not None:
                curr = curr.next
            curr.next = newnode

    # traversal
    def traverse(self):
        if self.head is None:
            print("empty head")
        else:
            curr = self.head
            # FIX: Loop until curr is None to print every node
            while curr is not None:
                # If it's the last node, just print data. Otherwise, add arrow.
                if curr.next is None:
                    print(curr.data)
                else:
                    print(curr.data, end=' -> ')
                curr = curr.next

# Testing the code
sll = SinglyLinkedList()
sll.traverse()       # Expected: empty head
sll.append(50)
sll.traverse()       # Expected: 50
sll.append(60)
sll.append(70)
sll.traverse()       # Expected: 50 -> 60 -> 70