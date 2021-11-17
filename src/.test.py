import datetime
from node import *
from dataStructure import *

n1 = Node(address='', year=20, month='February', day=28, hour=1, minute=15)
n2 = Node(address='', year=30, month=10, day=2, hour=1, minute=15)
n3 = Node(address='', year=15, month=10, day=2, hour=1, minute=10)
n4 = Node(address='', year=1, month='August', day=8, hour=0, minute=0)
# n5 = Node(address='', year=80, month=10, day=2, hour=1, minute=15)

l1 = LinkedListPictures()

l1.addNode(n1)
l1.addNode(n2)
l1.addNode(n3)
l1.addNode(n4)
# l1.addNode(n5)



print(l1.__repr__())