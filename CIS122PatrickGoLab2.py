#PatrickGoLab2.py
#Author: Patrick Go
#Date last modified: 02/05/21
# Purpose: To demonstrate how to use variables

#Program uses: to become familiar with debugging process, recognizing syntax errors, using IDLE

#Problem 1:

#Part 1:

#num_1 = 30
#num_2 = 25
#num_3 = 40
#3 hard coded variables

three_nums = [30, 25, 40]
#Storing in list for easier handling

avg_result = sum(three_nums) / len(three_nums)
#Calculate the average

#print(avg_result)

#Part 2:
any_three_nums = [] #Create list

#Grab 3 numbers from user
x = int(input("Please enter a value: "))
y = int(input("Please enter a value: "))
z = int(input("Please enter a value: "))

#Store 3 numbers in list
any_three_nums.append(x)
any_three_nums.append(y)
any_three_nums.append(z)

#Calculate average
avg_result_3 = sum(any_three_nums) / len(any_three_nums)

print(avg_result_3)


#Problem 3:

earth_weight = int(input("Please enter your earth weight: "))

moon_weight = earth_weight * 0.165

print(moon_weight)
