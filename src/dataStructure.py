from src.node import Node
from src.time import *

class LinkedListPictures:
    def __init__(self, pointer=None):
        self.length = 0
        self.pointer = pointer

    def addFirstNode(self, node=None):
        pass

    def addLastNode(self, node=None):
        pointer = self.pointer
        if pointer == None:
            self.pointer = Node(node)
            return
        while pointer.getNext() != None:
            pointer = pointer.getNext()
        pointer.setNext(Node(node))

    def getLength(self):
        return self.length

    def __str__(self):
        pass

