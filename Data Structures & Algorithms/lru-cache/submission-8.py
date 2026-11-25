class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev, self.nxt = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.nxt, self.right.prev = self.right, self.left

    def __insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        prev.nxt = nxt.prev = node
        node.prev, node.nxt = prev, nxt

    def __remove(self, node: Node):
        prev, nxt = node.prev, node.nxt
        prev.nxt = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if not self.cache.get(key):
            return -1
        
        n = self.cache.get(key)
        self.__remove(n)
        self.__insert(n)
        return n.val
        

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return None
        
        if self.cache.get(key):
            node = self.cache[key]
            node.val = value
            self.__remove(node)
            self.__insert(node)
            return
        
        node = Node(key, value)
        self.cache[key] = node
        self.__insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.nxt
            self.__remove(lru)
            del self.cache[lru.key]
        


        
