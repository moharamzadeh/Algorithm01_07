import datetime

class Node:
	def __init__(self, address, year, month, day, hour, minute, tag=False):
		self.address = address
		self.time = datetime.time(hour, minute)
		self.timeDate = []
		self.setTimeDate(year=year, month=month, day=day)
		self.tag = tag
		self.next = None
		self.previous = None

	def setTimeDate(self, year, month, day):
		self.timeDate = [year]
		if isinstance(month, int):
			self.timeDate.append(month)
		else:
			self.timeDate.append(self.changeDateToInt(month))
		self.timeDate.append(day)
		self.timeDate.append(self.getTotalSecond())


	def setData(self, address, year, month, day, hour, minute, tag=False):
		self.address = address
		self.time = datetime.time(hour, minute)
		self.timeDate = []
		self.setTimeDate(year=year, month=month, day=day)
		self.tag = tag

	def changeDateToInt(self, month: str):
		listMonth = {'january': 1,'february': 2, 'march':3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
		return listMonth[month.lower()]

	def changeIntToDate(self, month: int):
		listMonth = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july', 8: 'august', 9: 'september', 10: 'october', 11: 'november', 12: 'december'}
		return listMonth[month]

	def setNext(self, next):
		self.next = next

	def setPrevious(self, previous):
		self.previous = previous

	def getTotalSecond(self) -> int:
		time = datetime.timedelta(hours=self.time.hour, minutes=self.time.minute)
		totalSecond = int(time.total_seconds())
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

