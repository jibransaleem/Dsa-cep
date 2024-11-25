# -*- coding: utf-8 -*-
"""cep

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1czEe2NyB2FHO8xhFBudlXYWypgv36yO2
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.get_requests = 0
        self.misses = 0

    def get(self, key):
        self.get_requests += 1
        if key in self.hash:
            n = self.hash[key]
            self.remove(n)
            self.add(n)
            return n.val
        else:
            self.misses += 1
            return -1

    def put(self, key, value):
        if key in self.hash:
            n = self.hash[key]
            n.val = value
            self.remove(n)
            self.add(n)
        else:
            self.misses += 1
            if len(self.hash) >= self.capacity:
                lru = self.head.next
                self.remove(lru)
                del self.hash[lru.key]
            new_node = Node(key, value)
            self.add(new_node)
            self.hash[key] = new_node

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def add(self, node: Node):
        prev_node = self.tail.prev
        prev_node.next = node
        self.tail.prev = node
        node.prev = prev_node
        node.next = self.tail

    def miss_rate(self):
        total_requests = self.get_requests
        if total_requests == 0:
            return 100.0
        return (self.misses / total_requests) * 100