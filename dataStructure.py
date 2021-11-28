import datetime
from colorama import Fore
import colorama
from node import *

class LinkedListPictures:
	def __init__(self, node=None):
		self.pointer = node
		self.__printLog(object=self, operation='l')

	def addNode(self, node):	#If == Error	
		def addFirstNode(node):
			temp = self.pointer
			if temp is None:
				self.pointer = node
				self.__printLog(object=node, operation='a')
				self.__printLog(object=self, operation='l')
				return
			node.setNext(temp)
			temp.setPrevious(node)
			# node <-> self.pointer
			self.pointer = node
			# self.pointer -> node
			self.__printLog(object=node, operation='a')
			self.__printLog(object=self, operation='l')

		def addNextNode(inputNode, nodeInList):
			if nodeInList.getNext() is None:
				nodeInList.setNext(inputNode)
				inputNode.setPrevious(nodeInList)
				# nodeInList <-> inputNode
				self.__printLog(object=node, operation='a')
				self.__printLog(object=self, operation='l')
				return

			nextNode = nodeInList.getNext()

			inputNode.setNext(nextNode)
			nextNode.setPrevious(inputNode)
			# inputNode <-> nextNode
			nodeInList.setNext(inputNode)
			inputNode.setPrevious(nodeInList)
			# nodeInList <-> inputNode
			self.__printLog(object=node, operation='a')
			self.__printLog(object=self, operation='l')
		
		temp = self.searchNode(node)
		if temp is None:
			addFirstNode(node)
			return
		addNextNode(inputNode=node, nodeInList=temp)

	def addData(self, address, year, month, day, hour, minute, tag=False):
		node = Node(address=address, year=year, month=month, day=day, hour=hour, minute=minute, tag=tag)
		self.addNode(node)

	def existNode(self, node):
		temp = self.searchNode(node=node, equal=True)
		if temp is None:
			return False
		return True

	def searchNode(self, node, equal=False):
		def search(node):
			temp = self.pointer
			if node is None or temp is None:
				return None
			while temp.__cmp__(node) < 0 :
				if temp.next is None :
					return temp
				temp = temp.next
			if temp.__cmp__(node) > 0: 
				return temp.getPrevious()
			return temp

		temp = search(node)
		if temp is None:
			return None
		if equal is True:
			if temp.__cmp__(node) == 0:
				return temp
			return None

		return temp

	def searchNextNodeByTag(self, inputNode, tagIsImportant=None):
		def searchNextNodeTrue(node):
			if self.pointer is None:
				self.__printLog(object=inputNode, operation='nF')
				return None
			if node is None:
				if self.pointer.getTag() == True:
					self.__printLog(object=self.pointer, operation='sNT', logObject=inputNode)
					self.__printLog(object=self, operation='l')
					return self.pointer
				self.__printLog(object=inputNode, operation='nFNT')
				self.__printLog(object=self, operation='l')
				return None
			if node.getNext() is None:
				self.__printLog(object=inputNode, operation='nFNT')
				self.__printLog(object=self, operation='l')
				return None
			node = node.getNext()
			while node.getTag() != True:
				node = node.getNext()
				if node is None:
					self.__printLog(object=inputNode, operation='nFNT')
					self.__printLog(object=self, operation='l')
					return None
			self.__printLog(object=node, operation='sNT', logObject=inputNode)
			self.__printLog(object=self, operation='l')
			return node
		
		def searchNextNode(node):
			if self.pointer is None:
				self.__printLog(object=inputNode, operation='nFN')
				self.__printLog(object=self, operation='l')
				return None
			if node is None:
				self.__printLog(object=self.pointer, operation='sN', logObject=inputNode)
				self.__printLog(object=self, operation='l')
				return self.pointer
			if node.getNext() is None:
				self.__printLog(object=inputNode, operation='nFN')
				self.__printLog(object=self, operation='l')
				return None
			self.__printLog(object=node.getNext(), operation='sN', logObject=inputNode)
			self.__printLog(object=self, operation='l')
			return node.getNext()

		nodeInList = self.searchNode(inputNode)
		if tagIsImportant == True:
			return searchNextNodeTrue(nodeInList)
		return searchNextNode(nodeInList)
		
	def deleteNode(self, node):
		def deleteLastNode(node):
			preNode = node.getPrevious()
			preNode.setNext(None)
			self.__printLog(object=node, operation='d')
			self.__printLog(object=self, operation='l')
		
		def deleteFirstNode(node):
			nextNode = node.getNext()
			self.pointer = nextNode
			nextNode.setPrevious(None)
			self.__printLog(object=node, operation='d')
			self.__printLog(object=self, operation='l')

		def deleteBetweenNode(node):
			nextNode = node.getNext()
			preNode = node.getPrevious()
			preNode.setNext(nextNode)
			nextNode.setPrevious(preNode)
			# preNode <-> nextNode
			self.__printLog(object=node, operation='d')
			self.__printLog(object=self, operation='l')

		nodeInList = self.searchNode(node, equal=True)
		if nodeInList is None or node.__cmp__(nodeInList) != 0:
			self.__printLog(object=node, operation='nF')
			self.__printLog(object=self, operation='l')
			return
		
		# length(list) == 1
		if nodeInList == self.pointer and nodeInList.getNext() is None:
			self.pointer = None
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

	def __str__(self):
		data = ['pointer']
		node = self.pointer
		while node != None:
			data.append(str(node))
			node = node.getNext()
		data.append('None')
		return ' <> '.join(data)

	def __repr__(self):
		print(self)

	def __printLog(self, object, operation, logObject=''):
		operationDict = {
		'd': Fore.RED +'deleted',
		'a': Fore.LIGHTMAGENTA_EX + 'added',
		'l': Fore.CYAN + 'list',
		'nF': Fore.YELLOW + 'not found',
		'nFN': Fore.YELLOW + 'Not Found next node',
		'nFNT': Fore.YELLOW + 'Not Found next TRUE node',
		's': Fore.GREEN + 'search',
		'sN': Fore.GREEN + 'search next node',
		'sNT': Fore.GREEN + 'search next TRUE node'}
		print(operationDict[operation] + ' ' + str(logObject) + ' ' + Fore.RESET + str(object))