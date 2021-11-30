from colorama import Fore
from node import *

class LinkedListPictures:
	def __init__(self, node=None):
		self.pointer = node
		LinkedListPictures.__printLog(object=self, operation='l')

	def addNode(self, node):
		def addFirstNode(node):
			pointer = self.pointer
			if pointer is None:
				self.pointer = node
				LinkedListPictures.__printLog(object=node, operation='a')
				LinkedListPictures.__printLog(object=self, operation='l')
				return
			node.setNext(pointer)
			pointer.setPrevious(node)
			# node <-> self.pointer
			self.pointer = node
			# self.pointer -> node
			LinkedListPictures.__printLog(object=node, operation='a')
			LinkedListPictures.__printLog(object=self, operation='l')

		def addNextNode(inputNode, nodeInList):
			if nodeInList.getNext() is None:
				nodeInList.setNext(inputNode)
				inputNode.setPrevious(nodeInList)
				# nodeInList <-> inputNode
				LinkedListPictures.__printLog(object=node, operation='a')
				LinkedListPictures.__printLog(object=self, operation='l')
				return

			nextNode = nodeInList.getNext()

			inputNode.setNext(nextNode)
			nextNode.setPrevious(inputNode)
			# inputNode <-> nextNode
			nodeInList.setNext(inputNode)
			inputNode.setPrevious(nodeInList)
			# nodeInList <-> inputNode
			LinkedListPictures.__printLog(object=node, operation='a')
			LinkedListPictures.__printLog(object=self, operation='l')
		
		nodeInList = self.searchNode(node)
		if (nodeInList is not None) and (nodeInList == node):
			LinkedListPictures.__printLog(object=node, operation='ch', logObject=nodeInList)
			nodeInList.changeDataByNode(node)
			LinkedListPictures.__printLog(object=self, operation='l')
			return

		if nodeInList is None:
			addFirstNode(node)
			return
		addNextNode(inputNode=node, nodeInList=nodeInList)

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
			if node is None:
				LinkedListPictures.__printLog(object=self.pointer, operation='sNT', logObject=node)
				LinkedListPictures.__printLog(object=self, operation='l')
				return None
			for nodeInList in self:
				if nodeInList >= node and nodeInList.getTag() is True:
					LinkedListPictures.__printLog(object=nodeInList, operation='sNT', logObject=node)
					LinkedListPictures.__printLog(object=self, operation='l')
					return nodeInList
			LinkedListPictures.__printLog(object=node, operation='nFNT')
			LinkedListPictures.__printLog(object=self, operation='l')
			return None
		
		def searchNextNode(node):
			if node is None:
				LinkedListPictures.__printLog(object=self.pointer, operation='sN', logObject=node)
				LinkedListPictures.__printLog(object=self, operation='l')
				return self.pointer
			for nodeInList in self:
				if nodeInList >= node:
					LinkedListPictures.__printLog(object=nodeInList, operation='sN', logObject=node)
					LinkedListPictures.__printLog(object=self, operation='l')
					return nodeInList.getNext()
			LinkedListPictures.__printLog(object=node, operation='nFN')
			LinkedListPictures.__printLog(object=self, operation='l')
			return None

		if tagIsImportant == True:
			return searchNextNodeTrue(node)
		return searchNextNode(node)
		
	def deleteNode(self, node):
		def deleteLastNode(nodeInList):
			preNode = nodeInList.getPrevious()
			preNode.setNext(None)
			LinkedListPictures.__printLog(object=nodeInList, operation='d')
			LinkedListPictures.__printLog(object=self, operation='l')
		
		def deleteFirstNode(nodeInList):
			nextNode = nodeInList.getNext()
			self.pointer = nextNode
			nextNode.setPrevious(None)
			LinkedListPictures.__printLog(object=nodeInList, operation='d')
			LinkedListPictures.__printLog(object=self, operation='l')

		def deleteBetweenNode(nodeInList):
			nextNode = nodeInList.getNext()
			preNode = nodeInList.getPrevious()
			preNode.setNext(nextNode)
			nextNode.setPrevious(preNode)
			# preNode <-> nextNode
			LinkedListPictures.__printLog(object=nodeInList, operation='d')
			LinkedListPictures.__printLog(object=self, operation='l')

		for nodeInList in self:
			if nodeInList == node:
				# length(list) == 1
				if nodeInList == self.pointer and nodeInList.getNext() is None:
					self.pointer = None
					LinkedListPictures.__printLog(object=self, operation='l')
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
		# Not Found
		LinkedListPictures.__printLog(object=node, operation='nF')
		LinkedListPictures.__printLog(object=self, operation='l')

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

	def __printLog(object, operation, logObject=''):
		operationDict = {
		'd': Fore.RED +'deleted',
		'a': Fore.LIGHTMAGENTA_EX + 'added',
		'l': Fore.CYAN + 'list',
		'nF': Fore.YELLOW + 'not found',
		'nFN': Fore.YELLOW + 'Not Found next node',
		'nFNT': Fore.YELLOW + 'not found next TRUE node',
		's': Fore.GREEN + 'search',
		'sN': Fore.GREEN + 'search next node',
		'sNT': Fore.GREEN + 'search next TRUE node',
		'ch': Fore.YELLOW + 'change node'}
		print(operationDict[operation] + ' ' + str(logObject) + ' ' + Fore.RESET + str(object))