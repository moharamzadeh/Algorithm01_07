import datetime
from node import *

class LinkedListPictures:
	length = 0
	def __init__(self, node=None):
		self.pointer = node

	def addNode(self, node):	#If == Error
		temp = self.searchNode(node)
		
		if self.pointer == None:
			self.pointer = node
			return

		
		if temp.getNext() == None:	#If == Error
			self.addLastNode(node)
			return
				
		nextNode = temp.getNext()

		temp.setNext(node)
		node.setPrevious(temp)
		
		node.setNext(nextNode)
		nextNode.setPrevious(node)
		return
		
	def addLastNode(self, node):
		if self.pointer == None:
			self.pointer = node
			return
		
		temp = self.pointer
		while temp.getNext() != None:
			temp = temp.getNext()
		temp.setNext(node)
		node.setPrevious(temp)
		return

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

	def searchNode(self, node):
		temp = self.pointer
		if temp == None:
			return None
		while temp.__cmp__(node) < 0 :
			if temp.next == None :
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

