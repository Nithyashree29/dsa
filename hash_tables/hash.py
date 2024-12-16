class HashTable:
    def __init__(self, size):
        self.data = [None] * size  # Initialize an array of given size (None represents empty slots)

    def _hash(self, key):
        # Simple hash function that converts key to a numeric hash value
        hash_value = 0
        for i, char in enumerate(key):
            hash_value = (hash_value + ord(char) * i) % len(self.data)
        return hash_value

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []  # Initialize a list if the address is empty
        # Check if key exists, and update its value; otherwise, add a new key-value pair
        for item in self.data[address]:
            if item[0] == key:
                item[1] = value
                return self.data
        # If key doesn't exist, append the new key-value pair
        self.data[address].append([key, value])
        return self.data

    def get(self, key):
        address = self._hash(key)
        current_bucket = self.data[address]
        # print(current_bucket)
        if current_bucket:
            for item in current_bucket:
                if item[0] == key:
                    return item[1]
        return None  # Return None if key is not found

    def recursive_key(self, j):
        arr = []
        if len(j) == 1:
            arr.append(j[0][0])
        else:
            for i in range(len(j)):
                print("56789",j[0][0])
                arr.append(j[i][0])
        print("sssssssssss",arr)
        return arr
    def keys(self):
        keyArray =[]
        # print(self.data)
        for i in range(0,len(self.data)):
            # print(self.data[i])
            if self.data[i]:
                keyArray.extend(self.recursive_key(self.data[i]))
        return keyArray

# Example usage
my_hash_table = HashTable(10)
my_hash_table.set('grapes', 10000)
my_hash_table.get('grapes')  # Output: 10000
my_hash_table.set('apples', 9)
my_hash_table.set("shdfgjhas", 91)
# print(my_hash_table.get('apples'))  # Output: 9

print(my_hash_table.keys())




# One of our ZTM students with a great Discord username, mightypickachu, decided to enhance the previous keys() method to also include hash collision prevention. Here is how to do it (or you can try it yourself):

#  keys() {
#     if (!this.data.length) {
#       return undefined
#     }
#     let result = []
#     // loop through all the elements
#     for (let i = 0; i < this.data.length; i++) {
#         // if it's not an empty memory cell
#         if (this.data[i] && this.data[i].length) {
#           // but also loop through all the potential collisions
#           if (this.data.length > 1) {
#             for (let j = 0; j < this.data[i].length; j++) {
#               result.push(this.data[i][j][0])
#             }
#           } else {
#             result.push(this.data[i][0])
#           } 
#         }
#     }
#     return result; 
#   }