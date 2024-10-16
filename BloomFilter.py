class BloomFilter:
    def __init__(self, k, n):
        self.k = k
        self.size = n
        self.bit_array = 0

    def put(self, s):
        for i in range(self.k):
            index = mmh3.hash(s, i) % self.size
            self.bit_array |= (1 << index)

    def get(self, s):
        return all((self.bit_array & (1 << (mmh3.hash(s, i) % self.size))) != 0 for i in range(self.k))

    def get_size(self):
        return bin(self.bit_array).count('1') / self.k
