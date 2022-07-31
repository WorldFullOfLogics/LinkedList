class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, val, pos=-1):
        if self.head is None:
            if pos == 0 or pos == -1:
                newNode = Node(val)
                self.head = newNode
                self.tail = newNode
            else:
                return "Invalid position. List is empty"
        elif pos == -1:
            temp = self.tail
            self.tail = Node(val)
            temp.next = self.tail
        elif pos == 0:
            prev = self.head
            self.head = Node(val)
            self.head.next = prev
        else:
            cur = 1
            prev = self.head
            while prev:
                if cur == pos:
                    Next = prev.next
                    newNode = Node(val)
                    prev.next = newNode
                    newNode.next = Next
                    break
                cur += 1
                prev = prev.next
            else:
                return f"Invalid position: {pos}. List have only {cur - 1} elements"
        return "Element insertion to the list is successful"

    def __contains__(self, val):
        node = self.head
        while node:
            if node.value == val:
                return True
            node = node.next
        return False

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def delete(self, val):
        found = False
        if self.head is None:
            print("Invalid Operation! List is empty")
            return
        if self.head.value == val:
            found = True
            cur = self.head
            if cur.next is None:
                self.tail = None
            else:
                self.head = cur.next
                cur.next = None
        else:
            prev = self.head
            cur = prev.next
            while cur:
                if cur.value == val:
                    found = True
                    if cur.next is None:
                        self.tail = prev
                    Next = cur.next
                    prev.next = Next
                    cur.next = None
                    break
                prev = prev.next
                cur = prev.next
        if not found:
            print(f"{val} is not found in the list")


l1 = LinkedList()
l1.insert(29)
l1.insert(96)
l1.insert(80)

l1.delete(80)
l1.delete(0)
