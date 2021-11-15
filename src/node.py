import datetime

class Node:
    def __init__(self, address, year, month, day, hour, minute, second, tag=False, next=None, previous=None):
        self.address = address
        self.time = datetime.time(hour, minute, second)
        self.timeDate = [year, month, day, self.time]
        self.tag = tag
        self.next = next
        self.previous = previous

    def setData(self, address, year, month, day, hour, minute, second, tag=False):
        pass

    def setNext(self, next):
        self.next = next

    def setPrevious(self, previous):
        self.previous = previous

    def getTotalSecondList(self) -> list:
        time = datetime.timedelta(hours=self.timeDate[3].hour, minutes=self.timeDate[3].minute, seconds=self.timeDate[3].second)
        totalSecond = time.total_seconds()
        return [self.timeDate[0], self.timeDate[1], self.timeDate[2], totalSecond]

    def getData(self):
        pass

    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous

    def __str__(self):
        pass

    def __repr__(self):
        return self.timeDate
