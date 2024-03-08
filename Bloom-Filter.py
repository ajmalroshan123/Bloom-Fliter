import hashlib

class BloomFilter:
    def __init__(self,size, hash_function) :
        self.size = size
        self.bit_array = [0] * size
        self.hash_function = hash_function

    def add(self, item):
        for hsh_fn in self.hash_function:
            index = hsh_fn(item) % self.size
            self.bit_array[index] = 1

    def contains(self, item):
        for hsh_fn in self.hash_function:
            index = hsh_fn(item) % self.size
            if self.bit_array[index] == 0:
                return False
        return True

def hash_fucntion_1(item):
    return int(hashlib.md5(item.encode()).hexdigest(),16)

def hash_fucntion_2(item):
    return int(hashlib.sha256(item.encode()).hexdigest(),16)                

bloom_filter = BloomFilter(20, [hash_fucntion_1, hash_fucntion_2])

bloom_filter.add("apple")
bloom_filter.add("banana")
bloom_filter.add("orange")

print(bloom_filter.contains("apple"))
print(bloom_filter.contains("grape"))
