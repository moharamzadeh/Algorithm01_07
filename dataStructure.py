from node import *

class LinkedList:
	def __init__(self, node=None):
		self.pointer = node

	def addNode(self, node):
		def addFirstNode(inputNode):
			pointer = self.pointer
			if pointer is None:
				self.pointer = inputNode
				return
			inputNode.setNext(pointer)
			pointer.setPrevious(inputNode)
			# node <-> self.pointer
			self.pointer = inputNode
			# self.pointer -> node
			return

		def addNextNode(inputNode, nodeInList):
			if nodeInList.getNext() is None:
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
			return
		nodeInList = self.searchNode(node)
		if (nodeInList is not None) and (nodeInList == node):
			nodeInList.changeDataByNode(node)
			return 'change'

		if nodeInList is None:
			addFirstNode(node)
			return
		addNextNode(inputNode=node, nodeInList=nodeInList)
		return

	def addData(self, address, year, month, day, hour, minute, tag=False):
		node = Node(address=address, year=year, month=month, day=day, hour=hour, minute=minute, tag=tag)
		self.addNode(node)

	def existNode(self, node):
		for nodeInList in self:
			if nodeInList == node:
				return True
		return False

	def searchNode(self, node, equal=False):
		def search(inputNode):
			if inputNode is None:
				return None
			for node in self:
				if node > inputNode:
					return node.getPrevious()
				if node.getNext() is None:
					return node
			return None

		nodeInList = search(node)
		if equal is not True:
			return nodeInList
		if nodeInList == node:
			return nodeInList
		return None

	def searchNextNodeByTag(self, node, tagIsImportant=None):
		def searchNextNodeTrue(node):
			for nodeInList in self:
				if nodeInList > node and nodeInList.getTag() is True:
					return nodeInList
			return 'not found next TRUE node'
		
		def searchNextNode(node):
			for nodeInList in self:
				if nodeInList > node:
					return nodeInList
			return 'not found next node'

		if tagIsImportant == True:
			return searchNextNodeTrue(node)
		return searchNextNode(node)
		
	def deleteNode(self, node):
		def deleteLastNode(nodeInList):
			preNode = nodeInList.getPrevious()
			preNode.setNext(None)
		
		def deleteFirstNode(nodeInList):
			nextNode = nodeInList.getNext()
			self.pointer = nextNode
			nextNode.setPrevious(None)

		def deleteBetweenNode(nodeInList):
			nextNode = nodeInList.getNext()
			preNode = nodeInList.getPrevious()
			preNode.setNext(nextNode)
			nextNode.setPrevious(preNode)
			# preNode <-> nextNode

		def deleteNodeInList(nodeInList):
			# length(list) == 1
			if nodeInList == self.pointer and nodeInList.getNext() is None:
				self.pointer = None
				return
			# First Node
			if nodeInList == self.pointer:
				deleteFirstNode(nodeInList)
				return
			# Last Node
			if nodeInList.next is None:
				deleteLastNode(nodeInList)
				return
			# Between Node	
			deleteBetweenNode(nodeInList)
			return

		if (node != self.pointer) and (node.getNext() is None) and (node.getPrevious() is None):
			nodeInList = self.searchNode(node=node, equal=True)
		else:
			nodeInList = node

		if nodeInList is None:
			return None
		deleteNodeInList(nodeInList)
		return node

	def deleteNodeByTime(self, year, month, day, hour, minute):
		node = Node(address='', year=year, month=month, day=day, hour=hour, minute=minute)
		self.deleteNode(node)

	def __str__(self):
		data = ['pointer']
		node = self.pointer
		while node is not None:
			data.append(str(node))
			node = node.getNext()
		data.append('None')
		return ' <> '.join(data)

	def __repr__(self):
		print(self)

	def __iter__(self):		
		self.iterNode = self.pointer
		return self

	def __next__(self):
		if self.iterNode is None:
			raise StopIteration
		
		result = self.iterNode
		self.iterNode = self.iterNode.getNext()
		return result

	def __len__(self):
		pass
