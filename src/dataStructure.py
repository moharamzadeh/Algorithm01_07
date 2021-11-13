import datetime

class LinkedListPictures:
    length = 0
    def __init__(self, pointer=None):
        self.pointer = pointer

    def addFirstNode(self, node=None):
        node.next = self.pointer
        self.pointer = node

    def addLastNode(self, node=None):  # Error
        pointer = self.pointer
        if pointer == None:
            self.pointer = node
            return
        while pointer.getNext() != None:
            pointer = pointer.getNext()
        pointer.setNext(node)

    def getLength(self):
        return self.length

    def __str__(self):
        pass

    def __repr__(self):
        data = []
        node = self.pointer
        while node != None:
            data.append(str(node.getData()))
            node = node.getNext()
        data.append('None')
        return ' > '.join(data)

