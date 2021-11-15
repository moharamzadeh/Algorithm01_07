import datetime
from node import *
from dataStructure import *

n1 = Node(address='', year=2020, month=10, day=2, hour=1, minute=15, second=1)
l1 = LinkedListPictures(n1)

n2 = Node(address='', year=1390, month=10, day=2, hour=1, minute=15, second=2)
l1.addNextNode(n2)
# print(l1.__repr__())


n3 = Node(address='', year=2019, month=10, day=2, hour=1, minute=10, second=2)
n4 = Node(address='', year=2020, month=12, day=8, hour=0, minute=0, second=12)
n6 = Node(address='', year=1999, month=10, day=2, hour=1, minute=15, second=2)

l1.addNextNode(n3)
l1.addNextNode(n4)
l1.addNextData('', year=2020, month=9, day=30, hour=12, minute=10, second=59)
l1.addNextNode(n6)

print(l1.__repr__())