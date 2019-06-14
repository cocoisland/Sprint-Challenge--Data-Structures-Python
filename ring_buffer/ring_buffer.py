class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current < self.capacity:  # buffer not full
      self.storage[self.current] = item
      self.current += 1

    else:   # buffer is full
      self.current = 0
      self.storage[self.current] = item
      self.current += 1
    

  def get(self):
    return([i for i in self.storage if i is not None])

