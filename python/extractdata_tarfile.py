# check the current working directory
import os
os.getcwd()

# point to the location of the .tar file
path_tar = os.getcwd()+'/datasets/'+'datasets.tar'
path_tar

# extract the file with the images
import tarfile
tar = tarfile.open(path_tar)
tar.extractall()
tar.close()

# check the list of files extracted from tar file 
files = os.listdir(os.curdir) 
files
