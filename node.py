import datetime

class Node:
	next = None
	previous = None
	def __init__(self, address, year, month, day, hour, minute, tag=False):
		tempTimeDate = datetime.datetime(year=year, month=Node.changeDateToInt(month), day=1)
		delta = datetime.timedelta(days=day-1, hours=hour, minutes=minute)

		self.address = address
		self.dateTime = tempTimeDate + delta
		self.tag = tag

	def createNodeByTimeDate(year, month, day, hour, minute):
		node = Node(address='', year=year, month=Node.changeDateToInt(month), day=day, hour=hour, minute=minute)
		return node

	def changeDataByData(self, address, year, month, day, hour, minute, tag=False):
		node = Node(address=address, year=year, month=Node.changeDateToInt(month), day=day, hour=hour, minute=minute, tag=tag)
		self.changeDataByNode(node)

	def changeDataByNode(self, node):
		self.address = node.getAddress()
		self.dateTime = node.getDateTime()
		self.tag = node.getTag()

	def changeDateToInt(month):
		if isinstance(month, int):
			return month
		listMonth = {'january': 1,'february': 2, 'march':3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
		return listMonth[month.lower()]

	def changeIntToDate(month):
		if isinstance(month, str):
			return month
		listMonth = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july', 8: 'august', 9: 'september', 10: 'october', 11: 'november', 12: 'december'}
		return listMonth[month]

	def setNext(self, next):
		self.next = next

	def setPrevious(self, previous):
		self.previous = previous

	def setAddress(self, address):
		self.address == address

	def setTime(self, hour, minute):
		date = self.getDate()
		time = datetime.time(hour=hour, minute=minute)
		self.dateTime = datetime.datetime.combine(date=date, time=time)

	def setDate(self, year, month, day):
		date = datetime.date(year=year, month=Node.changeDateToInt(month), day=day)
		time = self.getTime()
		self.dateTime = datetime.datetime.combine(date=date, time=time)

	def setDateTime(self, year, month, day, hour, minute):
		self.dateTime = datetime.datetime(year=year, month=Node.changeDateToInt(month), day=day, hour=hour, minute=minute)

	def setTag(self, tag):
		self.tag = tag

	def getInformation(self):
		nodeInfo = (self.address, self.dateTime, self.tag)
		return nodeInfo
		# [address, date & time, tag]

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

	# self == node
	def __eq__(self, node):
		if self.__cmp__(node) == 0:
			return True
		return False

	# self != node
	def __ne__(self, node):
		if self.__cmp__(node) != 0:
			return True
		return False

	# self < node
	def __lt__(self, node):
		if self.__cmp__(node) == -1:
			return True
		return False

	# self <= node
	def __le__(self, node):
		if self.__cmp__(node) == -1 or self.__cmp__(node) == 0:
			return True
		return False

	# self > node
	def __gt__(self, node):
		if self.__cmp__(node) == 1:
			return True
		return False

	# self >= node
	def __ge__(self, node):
		if self.__cmp__(node) == 1 or self.__cmp__(node) == 0:
			return True
		return False

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
