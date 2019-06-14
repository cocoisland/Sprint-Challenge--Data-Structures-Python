class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if len(self.storage) <= self.capacity :
      self.storage.append(item)
    else:
      self.storage.pop(0)
      self.storage.append(item)

  def get(self):
    return(self.storage)