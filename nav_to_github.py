#Script to automatically navigate to GitHub/project-folder when run

import os
#Wait.. this scripts kinda pointless cos need to navigate to project folder to run.. hm.. add to desktop
print("Welcome! We will be navigating to the Github/project folder. \n")

curr_directory = os.getcwd()

print("As of right now, we are here: ", curr_directory)
curr_directory = os.chdir('/Users/patrick.go/Documents/GitHub/project-folder') #Navigate to this folder

print("\n Navigating..\n")

after_nav_dir = os.getcwd()

print("Success! We are here now: ", after_nav_dir)
