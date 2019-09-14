class RingBuffer: 
  def __init__(self, capacity): 
    self.capacity = capacity 
    self.current = 0 
    self.storage = [None]*capacity 

  def append(self, item): 
    oldest = self.current + 1 
    if oldest == self.capacity: 
      oldest = 0 

    self.storage[self.current] = item 
    self.current = oldest 
    
  def get(self): 
    return [i for i in self.storage if i]