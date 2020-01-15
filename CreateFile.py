#This program should automatically create Python files
import os
from datetime import datetime


timestr = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
dir_path = os.path.join('/Users/patrickgo/Desktop/Misc/project', timestr)
folder = os.mkdir(dir_path)

with open(os.path.join(dir_path, 'B' + timestr), 'w') as file:
    file.write('Exact time is: ' + timestr)
