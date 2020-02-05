#Creating folder using python
import os

path = "/Users/patrickgo/Desktop/Misc/NetDevEng"

#os.mkdir(path)

print(os.getcwd())
print("\n")
print("All of the files & folders in this directory are: \n",os.listdir())
#Prints current working directory + sublists & files
