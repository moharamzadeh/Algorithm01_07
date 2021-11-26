import datetime
from node import *
from dataStructure import *

# TODO: if == & search & sakht Node timeDate & deleteData & print porbar & cmp & length

n1 = Node(address='', year=2020, month=4, day=28, hour=1, minute=15)
n2 = Node(address='', year=2030, month=10, day=2, hour=1, minute=15)
n3 = Node(address='', year=2016, month=10, day=2, hour=0, minute=3)
n4 = Node(address='', year=2001, month=1, day=8, hour=0, minute=0)
n5 = Node(address='', year=2080, month=10, day=2, hour=1, minute=15)
n6 = Node(address='', year=2015, month=10, day=2, hour=0, minute=0)
n7 = Node(address='', year=2017, month=10, day=2, hour=0, minute=1)

l1 = LinkedListPictures()

l1.addNode(n1)
# print(l1.pointer.getNext())
l1.addNode(n2)
l1.addNode(n3)
l1.addNode(n4)
l1.addNode(n5)
l1.addNode(n6)
l1.addNode(n7)
print(l1.__repr__())

pic = Node(address='', year=2001, month=1, day=8, hour=0, minute=0)
l1.deleteNode(pic)
print(l1.__repr__())


pic = Node(address='', year=2020, month=4, day=28, hour=1, minute=15)
l1.deleteNode(pic)
print(l1.__repr__())