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
		if temp is None:
			return None
		while  temp.__cmp__(node) < 0 :
			if temp.next == None :
				return temp
			temp = temp.getNext()
		if temp.__cmp__(node) > 0: 
			return temp.getPrevious()
		return temp

	def deleteNode(self, node):
		pointer = self.searchNode(node)
		if  node.__cmp__(pointer) != 0 or pointer is None:
			print("The picture is not found")
			return
		
		if pointer.next is None:
			self.deleteLastNode(pointer)
		elif pointer.__cmp__(self.pointer) is 0:
			self.deleteFirstNode(node)
		else :	
			nextNode = pointer.getNext()
			preNode = pointer.getPrevious()
			preNode.setNext(nextNode)
			nextNode.setPervious(preNode)
		print("The picture successfully deleted")
		return
	
	def deleteLastNode(self, node):
		preNode = node.getPrevious()
		preNode.setNext(None)
		
	def deleteFirstNode(self, node):
		self.pointer = node.getNext()

	def deleteData(self, timeDate):
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

