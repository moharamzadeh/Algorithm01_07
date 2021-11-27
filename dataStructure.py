import datetime
from colorama import Fore
import colorama
from node import *

class LinkedListPictures:
	def __init__(self, node=None):
		self.pointer = node
		print(Fore.CYAN + 'Primary list: ' + Fore.RESET + self.__repr__())

	def addNode(self, node):	#If == Error	
		def addFirstNode(node):
			temp = self.pointer
			if temp == None:
				self.pointer = node
				print(Fore.LIGHTMAGENTA_EX + 'Added: ' + Fore.RESET + node.__repr__())
				print(Fore.CYAN + 'New list: ' + Fore.RESET + self.__repr__())
				return
			node.setNext(temp)
			temp.setPrevious(node)
			# node <-> self.pointer
			self.pointer = node
			# self.pointer -> node
			print(Fore.LIGHTMAGENTA_EX + 'Added: ' + Fore.RESET + node.__repr__())
			print(Fore.CYAN + 'New list: ' + Fore.RESET + self.__repr__())

		def addNextNode(inputNode, nodeInList):
			if nodeInList.getNext() == None:
				nodeInList.setNext(inputNode)
				inputNode.setPrevious(nodeInList)
				# nodeInList <-> inputNode
				print(Fore.LIGHTMAGENTA_EX + 'Added: ' + Fore.RESET + node.__repr__())
				print(Fore.CYAN + 'New list: ' + Fore.RESET + self.__repr__())
				return

			nextNode = nodeInList.getNext()

			inputNode.setNext(nextNode)
			nextNode.setPrevious(inputNode)
			# inputNode <-> nextNode
			nodeInList.setNext(inputNode)
			inputNode.setPrevious(nodeInList)
			# nodeInList <-> inputNode
			print(Fore.LIGHTMAGENTA_EX + 'Added: ' + Fore.RESET + node.__repr__())
			print(Fore.CYAN + 'New list: ' + Fore.RESET + self.__repr__())
		
		temp = self.searchNode(node)
		if temp == None:
			addFirstNode(node)
			return
		addNextNode(inputNode=node, nodeInList=temp)

	def addData(self, address, year, month, day, hour, minute, tag=False):
		node = Node(address=address, year=year, month=month, day=day, hour=hour, minute=minute, tag=tag)
		self.addNode(node)
		print(Fore.LIGHTMAGENTA_EX + 'Added: ' + Fore.RESET + node.__repr__())
		print(Fore.CYAN + 'New list: ' + Fore.RESET + self.__repr__())

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
		if temp == None: # print Err
			return self.pointer
		if temp.getNext() == None:
			print(Fore.YELLOW + '[Last Node] Not Found next node ' + node.__repr__() + Fore.RESET)
			return None
		if tag == None or tag == False:
			print(Fore.GREEN + 'Search next node ' + node.__repr__() + ':' + Fore.RESET, end=' ')
			print(temp.getNext().__repr__())
			return temp.getNext()
		temp = temp.getNext()
		while temp.getTag() != True:
			temp = temp.getNext()
			if temp == None:
				print(Fore.YELLOW + 'Not Found next node ' + node.__repr__() + Fore.RESET)
				return None
		print(Fore.GREEN + 'Search next node ' + node.__repr__() + ':' + Fore.RESET + node.__repr__(), end=' ')
		print(temp.__repr__())
		return temp

	def deleteNode(self, node):
		def deleteLastNode(node):
			preNode = node.getPrevious()
			preNode.setNext(None)
			print(Fore.RED + 'Deleted: ' + Fore.RESET + node.__repr__())
			print(Fore.CYAN + 'New list: ' + Fore.RESET + self.__repr__())
		
		def deleteFirstNode(node):
			nextNode = node.getNext()
			self.pointer = nextNode
			nextNode.setPrevious(None)
			print(Fore.RED + 'Deleted: ' + Fore.RESET + node.__repr__())
			print(Fore.CYAN + 'New list: ' + Fore.RESET + self.__repr__())

		def deleteBetweenNode(node):
			nextNode = node.getNext()
			preNode = node.getPrevious()
			preNode.setNext(nextNode)
			nextNode.setPrevious(preNode)
			# preNode <-> nextNode
			print(Fore.RED + 'Deleted: ' + Fore.RESET + node.__repr__())
			print(Fore.CYAN + 'New list: ' + Fore.RESET + self.__repr__())

		pointer = self.searchNode(node)
		if pointer == None or node.__cmp__(pointer) != 0:
			return
		
		# length(list) == 1
		if pointer == self.pointer and pointer.getNext() == None:
			self.pointer = None
			print(Fore.CYAN + 'New list: ' + Fore.RESET + self.__repr__())
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
		pass

	def __repr__(self):
		data = ['pointer']
		node = self.pointer
		while node != None:
			data.append(str(node.__repr__()))
			node = node.getNext()
		data.append('None')
		return ' <-> '.join(data)

