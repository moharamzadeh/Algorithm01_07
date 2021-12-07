from dataStructure import *

class LinkedListPictures(LinkedList):
	def __init__(self, node=None):
		super().__init__(node=node)
		LinkedListPictures.__printLog(object=self, operation='l')

	def addNode(self, node):
		result = super().addNode(node=node)
		if result == 'change':
			LinkedListPictures.__printLog(object=node, operation='ch', logObject=result)
			LinkedListPictures.__printLog(object=self, operation='l')
			return

		LinkedListPictures.__printLog(object=node, operation='a')
		LinkedListPictures.__printLog(object=self, operation='l')

	def addData(self, address, year, month, day, hour, minute, tag=False):
		super().addData(address, year, month, day, hour, minute, tag=tag)

	def existNode(self, node):
		return super().existNode(node)

	def searchNode(self, node, equal=False):
		return super().searchNode(node, equal=equal)

	def searchNextNodeByTag(self, node, tagIsImportant=None):
		result = super().searchNextNodeByTag(node, tagIsImportant=tagIsImportant)
		if str(result) == 'not found next TRUE node':
			LinkedListPictures.__printLog(operation='nFNT', logObject=node)
			LinkedListPictures.__printLog(object=self, operation='l')
			return
		if str(result) == 'not found next node':
			LinkedListPictures.__printLog(operation='nFN', logObject=node)
			LinkedListPictures.__printLog(object=self, operation='l')
			return

		if tagIsImportant is True:
			LinkedListPictures.__printLog(object=result, operation='sNT', logObject=node)
			LinkedListPictures.__printLog(object=self, operation='l')
			return result
			
		LinkedListPictures.__printLog(object=result, operation='sN', logObject=node)
		LinkedListPictures.__printLog(object=self, operation='l')
		return result

	def deleteNode(self, node):
		result = super().deleteNode(node)
		if result is None:
			LinkedListPictures.__printLog(object=node, operation='nF')
			LinkedListPictures.__printLog(object=self, operation='l')
			return
		LinkedListPictures.__printLog(object=node, operation='d')
		LinkedListPictures.__printLog(object=self, operation='l')
	
	def __printLog(operation, logObject='', object=''):
		operationDict = {
		'd': Fore.RED +'deleted',
		'a': Fore.LIGHTMAGENTA_EX + 'added',
		'l': Fore.CYAN + 'list',
		'nF': Fore.YELLOW + 'not found',
		'nFN': Fore.YELLOW + 'not found next node',
		'nFNT': Fore.YELLOW + 'not found next TRUE node',
		's': Fore.GREEN + 'search',
		'sN': Fore.GREEN + 'search next node',
		'sNT': Fore.GREEN + 'search next TRUE node',
		'ch': Fore.YELLOW + 'change node'}
		print(operationDict[operation] + ' ' + str(logObject) + ' ' + Fore.RESET + str(object))
