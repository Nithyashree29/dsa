class StackArray:
    def __init__(self):
        self.array = []

    def peek(self):
        if len(self.array) >1:
            return self.array[0]
    
    def push(self, data):
        self.array.append(data)
        return self.array
    
    def pop(self):
        if len(self.array) >1:
            return self.array[-1]
        else:
            return "Undefined"
        

obj1 = StackArray()
print(obj1.push(10))
print(obj1.push(20))
print(obj1.peek())
print(obj1.pop())