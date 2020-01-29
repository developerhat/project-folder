#The insult machine!

import random
#Lol wow! Just having fun here

#Pretty simple program idea
#Getting familiar with the random module

insult_list1 = ['greasy','ludicrous', 'vicious', 'dozy', 'idiotic', 'imbecilic', 'pointless', 'mindless', 'moronic']

insult_list2 = ['piece']

insult_list3 = ['close', 'close-grained', 'compact', 'compressed', 'concentrated']

insult_list4 = ['monkey','dog', 'cow', 'goat', 'sheep', 'miser', 'wiener','turtleneck']

insult_list5 = ['vomit', 'disgorge', 'emit', 'eject', 'regurgitate']


word_1 = random.choice(insult_list1)
word_2 = random.choice(insult_list2)
word_3 = random.choice(insult_list3)
word_4 = random.choice(insult_list4)
word_5 = random.choice(insult_list5)

print('You', word_1, word_2, 'of', word_3, word_4, word_5)
