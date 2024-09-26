


class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:
    def __init__(self,capacity):
        self.cap = capacity
        self.cache = {} # map key to node

        # left is LRU, right is most recently used
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    #pointer functions to remove node from list
    def remove(self, node):
        # remove the node from the middle. i.e. first node points to 3rd and 3rd node points to first. this deletes middle node
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    #pointer functions to add node at right of linked list
    def insert(self, node):
        # to insert, place inbetween the right pointer and the prev.
        prev, nxt = self.right.prev, self.right
        node.prev, node.next = prev, nxt
        prev.next, nxt.prev = node, node

    def get(self,key):
        # need to write functions to move recent used item to right of double linked listsss
        if key in cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self,key,value):
        ## add and remove functions
        if key in self.cache:
            # remove old node
            self.remove(self.cache[key])
            # add new node to the right.
        self.cache[key] = Node(key, value)  # this creates the node in the cache.
        self.insert(self.cache[key])  # this is to add it to the doubly linked list.
        if len(self.cache) > self.cap:
            #remove left Node from cache and remove Node also.
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]









cache = LRUCache(2) # 2 is the capacity.
## These commands adds elements to cache, removes and retrieves
cache.put(1,1)
cache.put(2,2)
cache.get(1)
cache.put(3,3)
cache.get(2)
cache.put(4,4)
cache.get(3)
cache.get(4)
