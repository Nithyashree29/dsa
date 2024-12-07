class ArrayCreater:
    def __init__(self) -> None:
        self.length = 0
        self.data  = []


    def get(self, index):
        if 0 <= index < self.length:
            return self.data[index]
        raise IndexError("index out of range")

    def push(self, item):
        self.data.append(item)
        self.length += 1
        # print(self.data)
        return self.length
    
    def pop(self):
        if self.length >0:
            self.data.pop()
            self.length -= 1
            return self.data
    
    def delete_index(self, index):
        if 0 < index < self.length:
            self.shift_items(index)
            item = self.data.pop()
            self.length -= 1 
            return item


    def shift_items(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]

obj1 = ArrayCreater()
# print(obj1.get(1))

obj1.push(1)
obj1.push(2)
obj1.push(5)
obj1.push(89)
obj1.get(1)
print(obj1.data)
obj1.delete_index(2)
obj1.shift_items(2)
print(obj1.data)
print(obj1.length)