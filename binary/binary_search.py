class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def __repr__(self):
        return f"Node value {self.value}"

class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, key):
        new_node =  Node(key)
        if self.root is None:
            self.root = new_node
            return self.root
        else:
            crr_node = self.root
            while(True):
                if key < crr_node.value:
                    if not crr_node.left:
                        crr_node.left = new_node
                        break
                    crr_node = crr_node.left
                else:
                    if not crr_node.right:
                        crr_node.right = new_node
                        break
                    crr_node = crr_node.right
        return self.root
    
    def lookup(self, value):
        if self.root is None:
            return False
        else:
            curr_node = self.root
            while(curr_node):
                if value < curr_node.value:
                    curr_node = curr_node.left
                elif value > curr_node.value:
                    curr_node = curr_node.right
                elif curr_node.value == value:
                    return True
            return False

    def remove(self, value):
        if not self.root:
            return False
        crr_node = self.root
        par_node = None
        while(crr_node):
            if value < crr_node.value:
                par_node = crr_node
                crr_node = crr_node.left
            elif value > crr_node.value:
                par_node = crr_node
                crr_node = par_node.right
            # elif crr_node.value = 




    def in_order_tracersal(self, node):
        if node:
            self.in_order_tracersal(node.left)
            print(node.value, end = ' ')
            self.in_order_tracersal(node.right)


obj1 = BinarySearchTree()
obj1.insert(1)
obj1.insert(5)
obj1.insert(6)
obj1.insert(8)
obj1.insert(9)
obj1.insert(3)
obj1.in_order_tracersal(obj1.root)
print(obj1.lookup(9))
print(obj1.lookup(98767890))

        