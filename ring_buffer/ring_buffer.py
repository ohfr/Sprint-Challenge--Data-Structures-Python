class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = []
        self.oldest = 0

    def append(self, item):
        if self.count < self.capacity:
            self.count +=1
            self.storage.append(item)
        else:
            self.storage[self.oldest] = item
            self.oldest +=1
            if self.oldest >= len(self.storage):
                self.oldest = 0

    def get(self):
        return self.storage