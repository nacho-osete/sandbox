"""
   Just a relaxed approach to the Infinite Monkey Theorem.
   Proof of Concept: not quite documented yet, I fear.

   More information and amenities there:
   https://en.wikipedia.org/wiki/Infinite_monkey_theorem
   https://youtu.be/yZS_vb549cc 
"""
import string
import random

def string_a_monkey(alphabase,length):
    monkey_string = ""
    str_length = len(length)

    for x in range(str_length):
        monkey_string = monkey_string + random.choice(alphabase)
    return monkey_string

def string_score(str_gen, str_comp):
    scorecount = 0.0
    str_length = len(str_gen)
    
    for i in range(str_length):
        if str_gen[i] != str_comp[i]: break
        scorecount = scorecount + (1 / str_length) * 100
    return scorecount     

def main():
    str_gen = ""
    str_score = 0
    str_dict = string.ascii_lowercase + " "
    str_comp = "methinks it is like a weasel"
  
    while str_score < 100:
        str_gen = string_a_monkey(str_dict, str_comp)
        str_score = string_score(str_gen, str_comp)
        print("%s <-- %02.2f" %(str_gen, str_score))
     

#InfiniMonkey!
main()