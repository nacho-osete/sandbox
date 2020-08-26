"""
   Annagrammer.

   An early brute-force proof-of-concept of 
   dirty anagram generator based in a thought-out-of-the box 
   loose algorithm that doesn't always work as expected.

   Just for fun and improvement at any time. Not very 
   good programming example but quite highly tinkable!

   Enjoy!
"""
import math
import os

os.system('clear')
# our string
a_string = "abcce"

# preallocate variables
word_list = [""] 
char_list = [""] * len(a_string)
char_tmp = ""
str_token = ""
new_word = ""

# we put our string in the first position of the final list
char_index = 0
word_list[0] = a_string
char_list = list(a_string)

for word_count in range (0, math.factorial(len(a_string))):
    
    for n in range (0, len(char_list)):
        
        for p in range (0, len(char_list)):

            # swapping characters
            char_tmp = char_list[n]
            char_list[n] = char_list[p]
            char_list[p] = char_tmp

            # new word
            new_word = str_token.join(char_list)
    
            # adding 'new' anagrams to word_list
            if new_word not in word_list:
                word_count = word_count + 1
                word_list.append(new_word)
    
    for n in range (len(char_list)-1, 0, -1):
        
        for p in range (len(char_list)-1, 0, -1):
               
            # swapping characters
            char_tmp = char_list[p]
            char_list[p] = char_list[n]
            char_list[n] = char_tmp

            # new word
            new_word = str_token.join(char_list)
    
            # adding 'new' anagrams to word_list
            if new_word not in word_list:
                word_count = word_count + 1
                word_list.append(new_word)

    for n in range (len(char_list)-1, 0, -1):
        
        for p in range (0, len(char_list)-1):
               
            # swapping characters
            char_tmp = char_list[p]
            char_list[p] = char_list[n]
            char_list[n] = char_tmp

            # new word
            new_word = str_token.join(char_list)
    
            # adding 'new' anagrams to word_list
            if new_word not in word_list:
                word_count = word_count + 1
                word_list.append(new_word)


    for n in range (0, len(char_list)-1):
        
        for p in range (len(char_list)-1, 0, -1):
               
            # swapping characters
            char_tmp = char_list[p]
            char_list[p] = char_list[n]
            char_list[n] = char_tmp

            # new word
            new_word = str_token.join(char_list)
    
            # adding 'new' anagrams to word_list
            if new_word not in word_list:
                word_count = word_count + 1
                word_list.append(new_word)


# finally, a probably (in)complete anagram list
print("%s, %d" % (word_list, len(word_list)))
