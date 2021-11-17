import datetime

class Node:
	def __init__(self, address, year, month, day, hour, minute, tag=False, next=None, previous=None):
		self.address = address
		self.time = datetime.time(hour, minute)
		self.timeDate = []
		self.setTimeDate(year=year, month=month, day=day)
		self.tag = tag
		self.next = next
		self.previous = previous

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
		self.timeDate = [year, month, day]
		self.timeDate.append(self.getTotalSecond())
		self.tag = tag

	def changeDateToInt(self, month: str):
		listMonth = {'January': 1,'February': 2, 'March':3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
		return listMonth[month]
	
	def changeIntToDate(self, month: int):
		listMonth = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
		return listMonth[month]

	def setNext(self, next):
		self.next = next

	def setPrevious(self, previous):
		self.previous = previous

	def getTotalSecond(self) -> list:
		time = datetime.timedelta(hours=self.time.hour, minutes=self.time.minute)
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

