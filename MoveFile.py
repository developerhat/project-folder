#This script should move whatever we give it

import os
import shutil

#Move file by renaming it's path
#os.rename('/Users/patrickgo/Desktop/Misc/project/B20200114-150613-769113.txt', '/Users/patrickgo/Desktop/Misc/Test/B20200114-150613-769113.txt')

#Use one or the other

source = '/Users/patrickgo/Desktop/Misc/project/B20200114-150613-769113.txt'
destination = '/Users/patrickgo/Desktop/Misc/Test/B20200114-150613-769113.txt'


# Move a file from the directory d1 to d2
shutil.move(source, destination)
