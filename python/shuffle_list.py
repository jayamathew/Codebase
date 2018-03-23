#shuffle elements in a list

#count the number of elements in the list
count_one = len(label_one)
print(count_one)

#create the original list 
list_one = list(range(0,count_one))
print(len(list_one))

#shuffle the elements in the list
from random import shuffle
shuffle(list_one)

print(list_one)