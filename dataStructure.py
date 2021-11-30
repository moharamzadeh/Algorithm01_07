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
		nodeInList = self.searchNode(node=node, equal=True)
		if nodeInList is None:
			return False
		return True

	def searchNode(self, node, equal=False):
		def search(node):
			nodeInList = self.pointer
			if node is None or nodeInList is None:
				return None
			while nodeInList < node :
				if nodeInList.next is None :
					return nodeInList
				nodeInList = nodeInList.next
			if nodeInList > node: 
				return nodeInList.getPrevious()
			return nodeInList

		nodeInList = search(node)
		if nodeInList is None:
			return None
		if equal is True:
			if nodeInList == node:
				return nodeInList
			return None

		return nodeInList

	def searchNextNodeByTag(self, inputNode, tagIsImportant=None):
		def searchNextNodeTrue(node):
			if self.pointer is None:
				LinkedListPictures.__printLog(object=inputNode, operation='nF')
				return None
			if node is None:
				if self.pointer.getTag() == True:
					LinkedListPictures.__printLog(object=self.pointer, operation='sNT', logObject=inputNode)
					LinkedListPictures.__printLog(object=self, operation='l')
					return self.pointer
				LinkedListPictures.__printLog(object=inputNode, operation='nFNT')
				LinkedListPictures.__printLog(object=self, operation='l')
				return None
			if node.getNext() is None:
				LinkedListPictures.__printLog(object=inputNode, operation='nFNT')
				LinkedListPictures.__printLog(object=self, operation='l')
				return None
			node = node.getNext()
			while node.getTag() != True:
				node = node.getNext()
				if node is None:
					LinkedListPictures.__printLog(object=inputNode, operation='nFNT')
					LinkedListPictures.__printLog(object=self, operation='l')
					return None
			LinkedListPictures.__printLog(object=node, operation='sNT', logObject=inputNode)
			LinkedListPictures.__printLog(object=self, operation='l')
			return node
		
		def searchNextNode(node):
			if self.pointer is None:
				LinkedListPictures.__printLog(object=inputNode, operation='nFN')
				LinkedListPictures.__printLog(object=self, operation='l')
				return None
			if node is None:
				LinkedListPictures.__printLog(object=self.pointer, operation='sN', logObject=inputNode)
				LinkedListPictures.__printLog(object=self, operation='l')
				return self.pointer
			if node.getNext() is None:
				LinkedListPictures.__printLog(object=inputNode, operation='nFN')
				LinkedListPictures.__printLog(object=self, operation='l')
				return None
			LinkedListPictures.__printLog(object=node.getNext(), operation='sN', logObject=inputNode)
			LinkedListPictures.__printLog(object=self, operation='l')
			return node.getNext()

		nodeInList = self.searchNode(inputNode)
		if tagIsImportant == True:
			return searchNextNodeTrue(nodeInList)
		return searchNextNode(nodeInList)
		
	def deleteNode(self, node):
		def deleteLastNode(node):
			preNode = node.getPrevious()
			preNode.setNext(None)
			LinkedListPictures.__printLog(object=node, operation='d')
			LinkedListPictures.__printLog(object=self, operation='l')
		
		def deleteFirstNode(node):
			nextNode = node.getNext()
			self.pointer = nextNode
			nextNode.setPrevious(None)
			LinkedListPictures.__printLog(object=node, operation='d')
			LinkedListPictures.__printLog(object=self, operation='l')

		def deleteBetweenNode(node):
			nextNode = node.getNext()
			preNode = node.getPrevious()
			preNode.setNext(nextNode)
			nextNode.setPrevious(preNode)
			# preNode <-> nextNode
			LinkedListPictures.__printLog(object=node, operation='d')
			LinkedListPictures.__printLog(object=self, operation='l')

		nodeInList = self.searchNode(node, equal=True)
		if (nodeInList is None) or (node != nodeInList):
			LinkedListPictures.__printLog(object=node, operation='nF')
			LinkedListPictures.__printLog(object=self, operation='l')
			return
		
		# length(list) == 1
		if nodeInList == self.pointer and nodeInList.getNext() is None:
			self.pointer = None
			LinkedListPictures.__printLog(object=self, operation='l')
			print(Fore.CYAN + 'List: ' + Fore.RESET + str(self))
		# First Node
		elif nodeInList == self.pointer:
			deleteFirstNode(nodeInList)
		# Last Node
		elif nodeInList.next is None:
			deleteLastNode(nodeInList)
		# Between Node
		else:	
			deleteBetweenNode(nodeInList)

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