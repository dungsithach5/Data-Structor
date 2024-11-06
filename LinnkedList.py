class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def list_all(self):
        t = self.head
        while t is not None:
            print(t.data, end='->')
            t = t.next
        print("None")

    def reverse_long(self):
        prev = None
        curr = self.head
        self.tail = self.head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def insert_after(self, pred, t):
        if pred is None:
            t.next = self.head
            self.head = t
        else:
            t.next = pred.next
            pred.next = t
        if pred is self.tail:
            self.tail = t

    def insert_head(self, x):
        new_node = Node(x)
        self.insert_after(None, new_node)

    def insert_tail(self, x):
        new_node = Node(x)
        self.insert_after(self.tail, new_node)

    def insert_sort(self):
        if self.is_empty():
            return
        pred = self.head
        curr = pred.next
        while curr is not None:
            subPred = None
            subCurr = self.head
            while subCurr.data < curr.data:
                subPred = subCurr
                subCurr = subCurr.next
            if subCurr == curr:
                pred = curr
            else:
                pred.next = curr.next
                if subPred  is None:
                    self.head = curr
                else:
                    subPred.next = curr
                curr.next = subCurr
            curr = pred.next
        self.tail = pred
        
        


if __name__ == "__main__":
    L = LinkedList()
    L.insert_tail(5), L.insert_tail(3), L.insert_tail(2), L.insert_tail(1), L.insert_tail(4)
    L.insert_sort(), L.list_all(), print()
    # L.reverse_long(), L.list_all()
