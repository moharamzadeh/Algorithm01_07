import datetime
from node import *
from dataStructure import *

n1 = Node(address='', year=2020, month='February', day=28, hour=1, minute=15)


l1 = LinkedListPictures(n1)


n2 = Node(address='', year=3390, month=10, day=2, hour=1, minute=15)

print(n1.__cmp__(n2))
print('s'.lower())

# l1.addNextNode(n2)
# # print(l1.__repr__())


# n3 = Node(address='', year=2019, month=10, day=2, hour=1, minute=10)
# n4 = Node(address='', year=2020, month='August', day=8, hour=0, minute=0)
# n6 = Node(address='', year=1999, month=10, day=2, hour=1, minute=15)

# l1.addNextNode(n3)
# l1.addNextNode(n4)
# l1.addNextData('', year=2020, month='July', day=30, hour=12, minute=10)
# l1.addNextNode(n6)

# print(l1.__repr__())