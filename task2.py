class EmptyBuffer(Exception):
    pass

class FullBuffer(Exception):
    pass

class CircularBuffer1:
    def __init__(self, size):
        self.size = size
        self.last_index = size - 1
        self.buffer = [None] * self.size
        self.rpointer = 0
        self.wpointer = 0
    
    def get(self):
        rpointer = self.rpointer
        value = self.buffer[rpointer]
        if value is None:
            raise EmptyBuffer
        self.buffer[rpointer] = None
        if rpointer == self.last_index:
            self.rpointer = 0
        else:
            self.rpointer = rpointer + 1
        return value
    
    def put(self, value):
        wpointer = self.wpointer
        if self.buffer[wpointer] is not None:
            raise FullBuffer

        self.buffer[wpointer] = value
        if wpointer == self.last_index:
            self.wpointer = 0
        else:
            self.wpointer = wpointer + 1


class BufNode:
    def __init__(self):
        self.value = None
        self.next = None

class CircularBuffer2:
    def __init__(self, size):
        root = BufNode()
        self.root = root

        cur_node = root
        for _ in range(size):
            cur_node.next = BufNode()
            cur_node = cur_node.next
        cur_node.next = root
        
        self.rpointer = root
        self.wpointer = root
    
    def get(self):
        rpointer = self.rpointer
        value = rpointer.value
        if value is None:
            raise EmptyBuffer
        
        self.rpointer = rpointer.next
        return value
    
    def put(self, value):
        wpointer = self.wpointer
        if wpointer.value is not None:
            raise FullBuffer
        wpointer.value = value
        self.wpointer = wpointer.next

import dis

dis.dis(CircularBuffer1.get)
dis.dis(CircularBuffer2.get)

dis.dis(CircularBuffer1.put)
dis.dis(CircularBuffer2.put)