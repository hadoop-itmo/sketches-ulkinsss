class CountingBloomFilter:
    def __init__(self, k, n, cap):
        self.k = k
        self.n = n
        self.cap = cap
        self.array = np.zeros((n // cap + 1, cap), dtype=np.uint32)
        self.t = list(range(k)) 

    def put(self, item):
        for t in self.t:
            index = mmh3.hash(item, t) % (self.n // self.cap)
            pos = t % self.cap
            if self.array[index][pos] < self.cap: 
                self.array[index][pos] += 1

    def get(self, item):
        for seed in self.t:
            index = mmh3.hash(item, seed) % (self.n // self.cap)
            if self.array[index][seed % self.cap] == 0:
                return False
        return True

    def get_size(self):

        return np.sum(self.array)/k
