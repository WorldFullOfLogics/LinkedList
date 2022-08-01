from LinkedListClass import Node


class circularLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node == self.tail:
                break
            node = node.next

    def insert(self, val, pos=-1):
        if self.head is None:
            if pos == 0 or pos == -1:
                self.head = Node(val)
                self.tail = self.head
                self.tail.next = self.head
                self.head.next = self.head
            else:
                print("Invalid position. List is empty")

        elif pos == 0:
            newNode = Node(val)
            next = self.head
            self.head = newNode
            self.head.next = next
            self.tail.next = self.head

        elif pos > 0 and pos != -1:
            cnt = 1
            prev = self.head
            while prev:
                if cnt == pos:
                    newNode = Node(val)
                    nextNode = prev.next
                    prev.next = newNode
                    newNode.next = nextNode
                    if prev == self.tail:
                        self.tail = newNode
                    break
                if prev == self.tail:
                    break
                cnt += 1
                prev = prev.next
            if pos - cnt:
                print(f"Invalid position: {pos}. List have only {cnt} elements")
        elif pos == -1:
            newNode = Node(val)
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head
        return "Element insertion to the list is successful"


l1 = circularLinkedList()
l1.insert(29)
l1.insert(34)
l1.insert(37)
l1.insert(80, 4)

print([node.value for node in l1])
