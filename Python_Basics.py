
LIST=['Book','Pen','Pencil'] # list

for i in LIST:
	print(i)    # prints "Book", "Pen", "Pencil"

for index,LIST in enumerate(LIST):
	print('#%d : %s'% (index,LIST)) # prints  "#0 : Book", "#1 : Pen", "#2 : Pencil"

DICT={'cat':1,'dog':2} # Dictionary	

for name,value in DICT.items():
	print(name,value)  # prints "cat 1", "dog 2"

SETS={'cat','dog','fish'} # Unordered collection of distinct elements

for index, SETS in enumerate(SETS):
	print('%d: %s'% (index,SETS))  # prints "0: fish", "1: dog", "2: cat"

TUPLE=(1,2)
print(TUPLE) # prints " (1,2) "

#USEFUL TRICK 

import numpy as np
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,16]])

indices=np.array([0,2,1,0])

print(a[np.arange(4),indices])  # prints "[ 1 7 10 13] "


