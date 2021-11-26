import datetime
from node import *

class LinkedListPictures:
	length = 0
	def __init__(self, node=None):
		self.pointer = node

	def addNode(self, node):	#If == Error	
		temp = self.searchNode(node)
		if temp == None:
			self.addFirstNode(node)
			return

		if temp.getNext() == None:	#If == Error
			self.addLastNode(node)
			return

		nextNode = temp.getNext()
		self.addNextNode(inputNode=node, node1=temp, node2=nextNode)

	def addData(self, address, year, month, day, hour, minute, tag=False):
		node = Node(address=address, year=year, month=month, day=day, hour=hour, minute=minute, tag=tag)
		self.addNode(node)

	def addFirstNode(self, node):
		pointer = self.pointer
		if pointer == None:
			self.pointer = node
			return
		node.setNext(pointer)
		pointer.setPrevious(node)
		# node <-> self.pointer
		self.pointer = node
		# self.pointer -> node

	def addLastNode(self, node):
		temp = self.pointer
		if temp == None:
			self.pointer = node
			return
		while temp.getNext() != None:
			temp = temp.getNext()
		temp.setNext(node)
		node.setPrevious(temp)
		# temp <-> node <-> None

	def addNextNode(self, inputNode, node1, node2):
		inputNode.setNext(node2)
		node2.setPrevious(inputNode)
		# inputNode <-> node2
		node1.setNext(inputNode)
		inputNode.setPrevious(node1)
		# node1 <-> inputNode

	def getLength(self):
		return self.length

	def searchNode(self, node):
		temp = self.pointer
		if node == None or temp == None:
			return None
		while temp.__cmp__(node) < 0 :
			if temp.next == None :
				return temp
			temp = temp.next
		if temp.__cmp__(node) > 0: 
			return temp.getPrevious()
		return temp

	def search(self, timeDate, tag):
		pass

	def deleteNode(self, node):
		pointer = self.searchNode(node)
		if pointer == None or node.__cmp__(pointer) != 0:
			print("The picture is not found")
			return
		
		if pointer.next == None:
			self.deleteLastNode(pointer)
		elif pointer == self.pointer:
			self.deleteFirstNode(pointer)
		else:	
			self.deleteBetweenNode(pointer)
		print("The picture successfully deleted")
	
	def deleteLastNode(self, node):
		preNode = node.getPrevious()
		preNode.setNext(None)
		
	def deleteFirstNode(self, node):
		nextNode = node.getNext()
		self.pointer = nextNode
		nextNode.setPrevious(None)

	def deleteBetweenNode(self, node):
		nextNode = node.getNext()
		preNode = node.getPrevious()
		preNode.setNext(nextNode)
		nextNode.setPrevious(preNode)
		# preNode <-> nextNode

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

