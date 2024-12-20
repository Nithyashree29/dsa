class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queues:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0


    def peek(self):
        return self.first

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        print(self.first.value, self.last.value)
        return self.first, self.last

    def dequeue(self):
        if not self.first:
            return "Undefined"
        elif self.first == self.last:
            self.last = None
        curr = self.first.value
        self.first = self.first.next
        self.length -= 1
        return curr



obj1 = Queues()
obj1.enqueue('Joy')
obj1.enqueue('Matt')



