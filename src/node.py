import datetime

class Node:
    def __init__(self, address, year, month, day, hour, minute, second, tag=False, next=None, previous=None):
        time = datetime.time(hour=hour, minute=minute, second=second)
        self.address = address
        self.timeDate = [year, month, day, time]
        self.tag = tag
        self.next = next
        self.previous = previous

    def setData(self, time, tag, next):
        pass

    def setNext(self, next):
        self.next = next

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
