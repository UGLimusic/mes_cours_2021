from LinkedList import *

lst = LinkedList()
lst.insert(3, 0)
lst.insert(2, 1)
lst.insert(1, 2)
lst.insert(4, 0)
lst2 = LinkedList()
lst2.insert(9, 0)
lst2.insert(8, 0)
lst2.insert(7, 0)
print(lst)
print(lst2)
lst.extend(lst2)
print(lst)
print(lst)
ls3 = LinkedList([4, 3, 2, 1, 7, 8, 9])
