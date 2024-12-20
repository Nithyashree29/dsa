class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):  #to see Top element
        return self.top.data

    def push(self, value):  #add node to top
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            curr = self.top
            self.top = new_node
            self.top.next = curr
        self.length += 1
        return self.top.data

        

    def pop(self):  #remove from top of the stack
        if self.top == self.bottom:
            curr = self.top.data
            self.top = self.top.next
            self.length -= 1
            return curr
        else:
            return "undefined"
    
obj1 = Stack()
print(obj1.push("google"))
print(obj1.push("Nithya"))
print(obj1.peek())
print(obj1.pop())