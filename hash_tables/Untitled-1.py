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
        if current_bucket:
            for item in current_bucket:
                if item[0] == key:
                    return item[1]
        return None  # Return None if key is not found

# Example usage
my_hash_table = HashTable(8)
my_hash_table.set('grapes', 10000)
print(my_hash_table.get('grapes'))  # Output: 10000
print(my_hash_table.set('apples', 9))
print(my_hash_table.get('apples'))  # Output: 9
