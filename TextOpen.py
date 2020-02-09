#Text file opener & reader program


#user_write = str(input("What would you like to write in the text file? "))
txt_file = open("myfile.txt", "a")
txt_file.write("Test! ")

txt_file = open("myfile.txt", "r")

print(txt_file.read())
