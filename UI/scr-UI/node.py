import datetime

class Node:
	def __init__(self, address, year, month, day, hour, minute, second, tag, next=None, previous=None):
		self.address = address
		self.time = datetime.time(hour, minute, second)
		self.timeDate = [year, month, day]
		self.timeDate.append(self.getTotalSecond())
		self.tag = tag
		self.next = next
		self.previous = previous

	def setData(self, address, year, month, day, hour, minute, second, tag=False):
		self.address = address
		self.time = datetime.time(hour, minute, second)
		self.timeDate = [year, month, day]
		self.timeDate.append(self.getTotalSecond())
		self.tag = tag

	def setNext(self, next):
		self.next = next

	def setPrevious(self, previous):
		self.previous = previous

	def getTotalSecond(self) -> list:
		time = datetime.timedelta(hours=self.time.hour, minutes=self.time.minute, seconds=self.time.second)
		totalSecond = time.total_seconds()
		return totalSecond

	def getTime(self):
		return self.time

	def getData(self):
		pass

	def getNext(self):
		return self.next
	
	def getPrevious(self):
		return self.previous

	def __cmp__(self, node):
		for i in range(len(self.timeDate)):
			if self.timeDate[i] > node.timeDate[i]:
				return 1
			elif self.timeDate[i] < node.timeDate[i]:
				return -1
		return 0

	def __repr__(self):
		return self.timeDate

