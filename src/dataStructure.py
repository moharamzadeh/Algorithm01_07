import datetime
from node import *

class LinkedListPictures:
	length = 0
	def __init__(self, node=None):
		self.pointer = node

	def addNextData(self, address, year, month, day, hour, minute, tag=False): 
		pointer = self.pointer
		node = Node(address, year, month, day, hour, minute, tag=False)
		if pointer == None:
			self.pointer = node
			return
		while pointer.getNext() != None:
			pointer = pointer.getNext()
		pointer.setNext(node)
		node.setPrevious(pointer)

	def addNextNode(self, node):
		pointer = self.pointer
		if pointer == None:
			self.pointer = node
			return
		while pointer.getNext() != None:
			pointer = pointer.getNext()
		pointer.setNext(node)
		node.setPrevious(pointer)

	def getLength(self):
		return self.length

	def searchNode(self, node):
		temp = self.pointer
		while  temp.__cmp__(node) < 0 :
			temp = temp.next
		if temp.__cmp__(node) > 0: 
			return temp.previous
		return temp

	def deleteNode(self, node):
		pass

	def deleteData(self, timeDate: list):
		pass

	def __str__(self):
		pass

	def __repr__(self):
		data = ['pointer']
		node = self.pointer
		while node != None:
			data.append(str(node.__repr__()))
			node = node.getNext()
		data.append('None')
		return ' <-> '.join(data)

