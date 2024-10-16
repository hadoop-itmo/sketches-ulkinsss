class Counter:
    def __init__(self, k: int, threshold: int):
        self.k = k
        self.threshold = threshold
        self.items = {}
        self.processed_count = 0
        self.frequent_items = {}

    def add_one(self, item: str):
        self.processed_count += 1

        if item in self.items:
            self.items[item] += 1
            if self.items[item] > self.threshold:
                self.frequent_items[item] = self.items[item]
        else:
            if len(self.items) < self.k - 1:
                self.items[item] = 1
            else:
                items_copy = self.items.copy()
                i = 0
                while i < len(items_copy):
                    key, value = list(items_copy.items())[i]
                    items_copy[key] = max(value - 1, 0)
                    if items_copy[key] == 0:
                        del items_copy[key]
                        i -= 1
                    i += 1
                self.items = items_copy

    def add(self, items: list):
        for item in items:
            self.add_one(item)

    def get(self, key: str):
        return self.items.get(key, 0)

    def get_frequent_items(self):
        return self.frequent_items

def find_keys(filename: str, k: int, threshold: int):
    h = Counter(k, threshold)

    with open(filename, 'r') as f:
        for line in f:
            items = line.split()
            h.add(items)

    return h.get_frequent_items()
