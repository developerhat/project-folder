def get_max_profit(stock_prices):
# given list of stock prices, determine maximum profit
# must buy before sell, cannot buy and sell at same time

# brute force approach:
# for every value, compare all values after it and calculate profit, record max profit and return that
  if len(stock_prices) < 2:
    raise ValueError('getting a profit requires at least 2 prices')

  max_profit = stock_prices[1] - stock_prices[0]

  for outer_time_index in range(len(stock_prices) - 1):
    for inner_time_index in range(outer_time_index + 1, len(stock_prices)):
      later_price = stock_prices[inner_time_index] #What are these next 2 lines doing? COnverintg to a list?
      earlier_price = stock_prices[outer_time_index]
      profit = later_price - earlier_price
      max_profit = max(profit, max_profit)

  return max_profit

#print(get_max_profit([40, 50, 110, 11, 12]))

#40, 50, 110, 11, 12

# 2nd task
# Write a function that takes a list of characters and reverses the letters in place
# (e.g. ) ["e","r","i","c"] -> ["c","i","r","e"]
#Must be in place function. Original list must be changed

def reverse_list(list):
    for i in list:
        return list[::-1]

def reverse_list(lst):
    lst.reverse()
    print (lst)






sam = ['a','c','p','g','f', 'y' ]

def reverse_char(chars_input, start_index = 0, end_index = 0):
  # iterate the list of characters, and start from 0 index
  # do the following when the difference between start and end indices are greater than 1
    # take start index and end index and swap their values
    # increment the start index by 1
    # increment the end index by -1
  # then you are done

  if end_index == 0:
      end_index = len(chars_input) - 1
  while start_index < end_index:
    chars_input[start_index], chars_input[end_index] = chars_input[end_index], chars_input[start_index]
    start_index = start_index +1
    end_index = end_index -1

reverse_char(sam)
print(sam)


#print reverse_char(chars)


message = [ 'c', 'a', 'k', 'e', ' ',
           'p', 'o', 'u', 'n', 'd', ' ',
           's', 't', 'e', 'a', 'l' ]



def reverse_word(chars_input):
  # reverse all characters in chars_input
  #Only run reverse in characters of the word. The differentiator is the ' '
  #Iterate until hitting a space
  # From 1st to space, just reverse all except for the space. Keep going until you find another space. Keep doing until reach end of array. Then reverse back the word
  #Need to reverse back words after initial reverse
  #For every character

  #Start index always 0, end index is always length -1..
  #Find start index of every word, then skip this word


  #How do you identify these numbers? That's the answer in order ot not hard code
  #The numbers are 0,4,6,10, etc.
  reverse_char(chars_input)
  reverse_char(chars_input, 0, 4)

  reverse_char(chars_input, 6, 10)
  reverse_char(chars_input, 12, 15)

reverse_word(message)
print(message)


# expect message now to be [ 's', 't', 'e', 'a', 'l', ' ',
          #  'p', 'o', 'u', 'n', 'd', ' ',
            # 'c', 'a', 'k', 'e',]
