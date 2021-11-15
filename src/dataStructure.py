import datetime
from node import *

class LinkedListPictures:
    length = 0
    def __init__(self, node=None):
        self.pointer = node

    def addFirstNode(self, node=None):
        node.next = self.pointer
        self.pointer = node

    def addNextNode(self, address, year, month, day, hour, minute, second, tag=False):  # Error
        pointer = self.pointer
        node = Node(address, year, month, day, hour, minute, second)
        if pointer == None:
            self.pointer = node
            return
        
        n = self.pointer

        while pointer.getNext() != None:
            pointer = pointer.getNext()
        pointer.setNext(node)
        pointer.setPrevious(n)

    def getLength(self):
        return self.length

    def __str__(self):
        pass

    def __repr__(self):
        data = []
        node = self.pointer
        while node != None:
            data.append(str(node.__repr__()))
            node = node.getNext()
        data.append('None')
        return ' > '.join(data)

