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
			if temp == None:
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
			if nodeInList.getNext() == None:
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
		if temp == None:
			addFirstNode(node)
			return
		addNextNode(inputNode=node, nodeInList=temp)

	def addData(self, address, year, month, day, hour, minute, tag=False):
		node = Node(address=address, year=year, month=month, day=day, hour=hour, minute=minute, tag=tag)
		self.addNode(node)

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

	def searchNextNodeByTag(self, inputNode, tagIsImportant=None):
		def searchNextNodeTrue(node):
			if self.pointer == None:
				print(Fore.YELLOW + '[List is empty] Not Found TRUE next node ' + str(inputNode) + Fore.RESET + Fore.RESET)
				return None
			if node == None:
				if self.pointer.getTag() == True:
					print(Fore.GREEN + 'Search next TRUE node ' + str(inputNode) + ':' + Fore.RESET, end=' ')
					print(str(self.pointer))
					return self.pointer
				print(Fore.YELLOW + 'Not Found next TRUE node ' + str(inputNode) + Fore.RESET)
				return None
			if node.getNext() == None:
				print(Fore.YELLOW + '[Last Node] Not Found next TRUE node ' + str(inputNode) + Fore.RESET)
				return None
			node = node.getNext()
			while node.getTag() != True:
				node = node.getNext()
				if node == None:
					print(Fore.YELLOW + 'Not Found next TRUE node ' + str(inputNode) + Fore.RESET)
					return None
			print(Fore.GREEN + 'Search next TRUE node ' + str(inputNode) + ':' + Fore.RESET, end=' ')
			print(node)
			return node
		
		def searchNextNode(node):
			if self.pointer == None:
				print(Fore.YELLOW + '[List is empty] Not Found next node ' + str(inputNode) + Fore.RESET + Fore.RESET)
				return None
			if node == None:
				print(Fore.GREEN + 'Search next node ' + str(inputNode) + ':' + Fore.RESET, end=' ')
				print(self.pointer)
				return self.pointer
			if node.getNext() == None:
				print(Fore.YELLOW + '[Last Node] Not Found next node ' + inputNode.__str__() + Fore.RESET)
				return None
			print(Fore.GREEN + 'Search next node ' + str(inputNode) + ':' + Fore.RESET, end=' ')
			print(node.getNext())
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

		pointer = self.searchNode(node)
		if pointer == None or node.__cmp__(pointer) != 0:
			self.__printLog(object=node, operation='nF')
			self.__printLog(object=self, operation='l')
			return
		
		# length(list) == 1
		if pointer == self.pointer and pointer.getNext() == None:
			self.pointer = None
			print(Fore.CYAN + 'List: ' + Fore.RESET + str(self))
		# First Node
		elif pointer == self.pointer:
			deleteFirstNode(pointer)
		# Last Node
		elif pointer.next == None:
			deleteLastNode(pointer)
		# Between Node
		else:	
			deleteBetweenNode(pointer)

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
		operationDict = {'d': Fore.RED + 'deleted', 'a': Fore.LIGHTMAGENTA_EX + 'added', 'l': Fore.CYAN + 'list', 'nF': Fore.YELLOW + 'not found', 's': Fore.GREEN + 'search', 'sN': Fore.GREEN + 'search next node'}
		print(operationDict[operation] + ' ' + str(logObject)+ Fore.RESET + str(object))