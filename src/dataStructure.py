import datetime
from node import *

class LinkedListPictures:
	length = 0
	def __init__(self, node=None):
		self.pointer = node

	def addNode(self, node):	#If == Error
		if self.pointer == None:
			self.pointer = node
			return

		if self.pointer.getNext() == None:	#If == Error
			if node.__cmp__(self.pointer) >= 0:
				self.pointer.setNext(node)
				node.setPrevious(self.pointer)
				return
			
			temp = self.pointer
			self.pointer = node
			node.setNext(temp)
			temp.setPrevious(node)
			return

		
		previousNode = self.searchNode(node)
		if previousNode == None:
			temp = self.pointer
			self.pointer = node
			node.setNext(temp)
			temp.setPrevious(node)
			return

		self.addNextNode(node, previousNode)
		

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

	def addNextNode(self, nodeInput: Node, nodeAddress: Node):
		pointer = nodeAddress.getNext()
		if pointer == None:
			nodeAddress.setNext(nodeInput)
			nodeInput.setPrevious(nodeAddress)
			return
		
		nodeAddress.setNext(nodeInput)
		nodeInput.setPrevious(nodeAddress)
		
		nodeInput.setNext(pointer)
		pointer.setPrevious(nodeInput)

	def getLength(self):
		return self.length

	def searchNode(self, node: Node):
		temp = self.pointer
		while  temp.__cmp__(node) < 0:
			if temp.next == None:
				return temp
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

