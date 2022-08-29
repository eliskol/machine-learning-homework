class HashTable:
    def __init__(self, num_buckets=5):
        self.num_buckets = num_buckets
        self.buckets = [[] for i in range(self.num_buckets)]

    def hash(self, string):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        hash_list = []

        for letter in string:
            hash_list.append(alphabet.index(letter))

        return sum(hash_list) % self.num_buckets

    def insert(self, key, value):
        bucket_index = self.hash(key)
        self.buckets[bucket_index].append((key, value))

    def find(self, key):
        bucket_index = self.hash(key)
        for pair in self.buckets[bucket_index]:
            if pair[0] == key:
                return pair[1]


ht = HashTable(num_buckets=3)
print(ht.buckets)
print(ht.hash('cabbage'))
ht.insert('cabbage', 5)
print(ht.buckets)
ht.insert('cab', 20)
print(ht.buckets)
print(ht.find('cabbage'))
print(ht.find('cab'))