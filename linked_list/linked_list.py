class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last_node = new_node
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def prepend(self, data ):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        curr_node = self.head
        while curr_node.next and curr_node.next.data != data:
            curr_node = curr_node.next
        if curr_node.next:
            curr_node = curr_node.next.next