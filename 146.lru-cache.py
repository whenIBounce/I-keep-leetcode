class DLinkedNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        cur = self.cache.get(key)
        # move cur to the head of the DLinkedNode list
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
    
        cur.next = self.head.next
        self.head.next.prev = cur 
        self.head.next = cur
        cur.prev = self.head
        
        return cur.val

    def put(self, key: int, value: int) -> None:
        # Update an existing node
        if key in self.cache:
            cur = self.cache.get(key)
            cur.val = value
            # move cur to the head of the DLinkedNode list
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
    
            cur.next = self.head.next
            self.head.next.prev = cur 
            self.head.next = cur
            cur.prev = self.head
            return
        # Add a new node
        if self.size == self.capacity:
            # get rid of the least used one
            leastUsedNode = self.tail.prev
            leastUsedNode.prev.next = self.tail
            self.tail.prev = leastUsedNode.prev
            # Shall I set leastUsedNode.prev and .next to None?
            # Add the new Node to the head
            cur = DLinkedNode(key, value)
            cur.next = self.head.next
            self.head.next.prev = cur 
            self.head.next = cur
            cur.prev = self.head
            # Add the new node to the cache
            del self.cache[leastUsedNode.key]
            self.cache[key] = cur
        else:
            self.size += 1
            # Add the new Node to the head
            cur = DLinkedNode(key, value)
            cur.next = self.head.next
            self.head.next.prev = cur 
            self.head.next = cur
            cur.prev = self.head
            # Add the new node to the cache
            self.cache[key] = cur
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Testing code
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1)) # prints 1
obj.put(3, 3) # evicts key 2
print(obj.get(2)) # prints -1
obj.put(4, 4) # evicts key 1
print(obj.get(1)) # prints -1
print(obj.get(3)) # prints 3
print(obj.get(4)) # prints 4