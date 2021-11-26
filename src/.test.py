import datetime
from node import *
from dataStructure import *

# TODO: if == & search & sakht Node timeDate & deleteData & print porbar & cmp & length & changeInfo (parameter na mahdod) & delete ==None and write is None

# NOTE: moghe delete az method search estefadeh mikoni? chon ghabli momkene bashe na khodesh

n1 = Node(address='', year=2020, month=4, day=28, hour=1, minute=15, tag=False)
# n2 = Node(address='', year=2030, month=10, day=2, hour=1, minute=15, tag=False)
# n3 = Node(address='', year=2070, month=10, day=2, hour=0, minute=3, tag=False)
# n4 = Node(address='', year=2000, month=1, day=8, hour=0, minute=0, tag=False)
# n5 = Node(address='', year=2090, month=10, day=2, hour=1, minute=15, tag=False)
# n6 = Node(address='', year=2015, month=10, day=2, hour=0, minute=0, tag=False)
# n7 = Node(address='', year=2045, month=10, day=2, hour=0, minute=1, tag=False)

l1 = LinkedListPictures()

l1.addNode(n1)
# print(l1.pointer.getNext())
# l1.addNode(n2)
# l1.addNode(n3)
# l1.addNode(n4)
# l1.addNode(n5)
# l1.addNode(n6)
# l1.addNode(n7)
print(l1.__repr__())

pic = Node(address='', year=2020, month=4, day=28, hour=1, minute=15, tag=False)
l1.deleteNode(n1)
print(l1.__repr__())