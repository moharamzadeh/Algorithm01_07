class Node:
    def __init__(self, time=None, tag=False, next=None, previous=None):
        self.time = time
        self.tag = tag
        self.next = next
        self.previous = previous

    def setData(self, time, tag, next):
        pass

    def setNext(self, next):
        pass

    def setPrevious(self, previous):
        pass

    def getData(self):
        pass

    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous

    def __str__(self):
        pass
