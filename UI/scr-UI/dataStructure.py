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
		self.addNextNode(inputNode=node, nodeInList=temp)

	def addData(self, address, year, month, day, hour, minute, tag=False):
		node = Node(address=address, year=year, month=month, day=day, hour=hour, minute=minute, tag=tag)
		self.addNode(node)

	def addFirstNode(self, node):
		temp = self.pointer
		if temp == None:
			self.pointer = node
			return
		node.setNext(temp)
		temp.setPrevious(node)
		# node <-> self.pointer
		self.pointer = node
		# self.pointer -> node

	def addNextNode(self, inputNode, nodeInList):
		if nodeInList.getNext() == None:
			nodeInList.setNext(inputNode)
			inputNode.setPrevious(nodeInList)
			# nodeInList <-> inputNode
			return

		nextNode = nodeInList.getNext()

		inputNode.setNext(nextNode)
		nextNode.setPrevious(inputNode)
		# inputNode <-> nextNode
		nodeInList.setNext(inputNode)
		inputNode.setPrevious(nodeInList)
		# nodeInList <-> inputNode

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

	def searchNextNodeByTag(self, node, tag=None):
		temp = self.searchNode(node)
		if temp == None or temp.getNext() == None:
			print('Not Found: Last Node')
			return None

		if tag == None or tag == False:
			return temp.getNext()

		while temp.getTag() != True:
			temp = temp.getNext()
			if temp == None:
				print('Not Found: Not exist')
				return None
		return temp

	def deleteNode(self, node):
		pointer = self.searchNode(node)
		if pointer == None or node.__cmp__(pointer) != 0:
			print("The picture is not found")
			return
		
		# length(list) == 1
		if pointer == self.pointer and pointer.getNext() == None:
			self.pointer = None
		# First Node
		elif pointer == self.pointer:
			self.deleteFirstNode(pointer)
		# Last Node
		elif pointer.next == None:
			self.deleteLastNode(pointer)
		# Between Node
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

