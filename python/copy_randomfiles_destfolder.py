#copy a random list of files from one folder to another to balance the count of class_0/class_1 files
import shutil
import os

source_class0 = r'C:\Users\...\class_0'
source_class1 = r'C:\Users\...\class_1'
dest0 = r'C:\Users\...\test\class_0'
dest1 = r'C:\Users\...\test\class_1'

files_class0 = os.listdir(source_class0)
print(len(files_class0))

files_class1 = os.listdir(source_class1)
print(len(files_class1))
#files_class0

#shuffle the elements in the list in class-1 as there are more compared to class-0
from random import shuffle
shuffle(files_class1)

files_class1_subset = files_class1[0:58]

len(files_class1_subset)

#copy label=0 to new folder
for file_name in files_class0:
    full_file_name = os.path.join(source_class0, file_name)
    if (os.path.isfile(full_file_name)):
        shutil.copy(full_file_name, dest0)

#copy label=1 to new folder
for file_name in files_class1_subset:
    full_file_name = os.path.join(source_class1, file_name)
    if (os.path.isfile(full_file_name)):
        shutil.copy(full_file_name, dest1)