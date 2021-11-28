import datetime

class Node:
	def __init__(self, address, year, month, day, hour, minute, tag=False):
		self.address = address
		self.dateTime = datetime.datetime(year=year, month=self.changeDateToInt(month), day=day, hour=hour, minute=minute)
		self.tag = tag
		self.next = None
		self.previous = None

	def changeData(self, address, year, month, day, hour, minute, tag=False):
		self.address = address
		self.dateTime = datetime.datetime(year=year, month=self.changeDateToInt(month), day=day, hour=hour, minute=minute)
		self.tag = tag

	def createNodeTimeDate(self, timeDate):
		pass

	def changeDateToInt(self, month):
		if isinstance(month, int):
			return month
		listMonth = {'january': 1,'february': 2, 'march':3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
		return listMonth[month.lower()]

	def changeIntToDate(self, month):
		if isinstance(month, str):
			return month
		listMonth = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july', 8: 'august', 9: 'september', 10: 'october', 11: 'november', 12: 'december'}
		return listMonth[month]

	def setNext(self, next):
		self.next = next

	def setPrevious(self, previous):
		self.previous = previous

	def getInformation(self):
		nodeInfo = (self.address, self.dateTime, self.tag)
		return nodeInfo # [address, date & time, tag]

	def printInformation(self, index=None):
		if index is None:
			print(self.getInformation
			()[0] + '  ' + str(self.getInformation()[1]) + '  ' + str(self.getInformation()[2]))
			return self.getInformation()
		info = self.getInformation()[index]
		print(info)
		return info

	def getAddress(self):
		return self.address

	def getTime(self):
		return self.dateTime.time()

	def getDate(self):
		return self.dateTime.date()

	def getDateTime(self):
		return self.dateTime

	def getNext(self):
		return self.next

	def getPrevious(self):
		return self.previous

	def getTag(self):
		return self.tag

	def __cmp__(self, node):
		if self.getDateTime() > node.getDateTime():
			return 1
		elif self.getDateTime() < node.getDateTime():
			return -1
		return 0

	def __str__(self):
		node = [str(self.dateTime), str(self.tag)]
		return ' '.join(node)

	def __repr__(self):
		print(self)
