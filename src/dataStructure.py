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
		if node.__cmp__(pointer) is 0 :
			if pointer.next is None:
				self.deleteLastNode(pointer)
			elif node.__cmp__(self.pointer) is 0:
				self.deleteFirstNode(node)
			else :	
				pointer = pointer.next
				pointer.pervious=pointer.next
			print("The picture successfully deleted")
			return
		print("The picture is not found")

	def deleteLastNode(self, node):
		preNode = node.getPrevious()
		preNode.setNext(None)
		# temp = self.searchNode(node)
		# pointer = temp.pervious
		# pointer.addNextNode(None)
		
	def deleteFirstNode(self, node):
		# temp = self.pointer
		# self.pointer = temp.next
		# del temp
		pass

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

