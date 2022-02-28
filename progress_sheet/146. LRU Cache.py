
class LRUCache:

    def __init__(self, capacity: int):
        if capacity >= 0:
            self.capacity = capacity
            self.dic = {}
            self.deq =deque([])
            
    def get(self, key: int) -> int:
        if key in self.dic:
            self.key_position_in_queue_handler(key)
            return self.dic[key]
        
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.dic:
            self.dic[key] = value
            self.key_position_in_queue_handler(key)
            
        else:
            
            if len(self.deq) < self.capacity:
                self.dic[key] = value
                self.deq.appendleft(key)
        
            else:
                self.dic.pop(self.deq.pop())
                self.dic[key] = value
                self.deq.appendleft(key)

    def key_position_in_queue_handler(self,key):
        temp = []
        while self.deq[-1] != key:
            temp.append(self.deq.pop())
            
        self.deq.appendleft(self.deq.pop())
        
        while temp:
            self.deq.append(temp.pop())

            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
