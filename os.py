import os

os.chdir('/Users/patrick.go/Desktop/')
print(os.getcwd())

os.chdir('/Users/patrick.go/Documents/GitHub/project-folder') #Navigate to this folder
os.rename('OS.py', 'os.py')

print('Home directory is: ', os.environ.get('HOME'))
file_path = os.path.join(os.environ.get('HOME'), 'os.py')
print(file_path)

for dirpath, dirnames, filenames in os.walk('/Users/patrick.go/Documents/GitHub/project-folder'):
    print('Current Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()

#print(os.stat('os.py')) #Returns stats of file
print(os.getcwd())
