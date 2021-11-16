import datetime
from node import *

class LinkedListPictures:
	length = 0
	def __init__(self, node=None):
		self.pointer = node

	def addNextData(self, address, year, month, day, hour, minute, second, tag=False): 
		pointer = self.pointer
		node = Node(address, year, month, day, hour, minute, second)
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
		pass

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

