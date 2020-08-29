from pythonds3 import Deque
from os import system
from time import sleep

system('clear')

def pal_checker(my_string):

    tmpDeque = Deque()
    isPalindrome = True

    for i in my_string:
        # Whitespace and Weird Symbols support ;-)
        if i not in " ',-!?": 
            tmpDeque.add_rear(i.lower())

    while tmpDeque.size() > 1:
        #print(tmpDeque._items)
        if tmpDeque.remove_rear() != tmpDeque.remove_front():
            isPalindrome = False

    return isPalindrome

# Inspired by Al Yankovic's Palindromes (just run and watch 'Bob' at the same time https://www.youtube.com/watch?v=gAfIikFnvuI)
palList1 =  [ "I, man, am regal - a German am I", "Never odd or even", "If I had a hi-fi", "Madam, I'm Adam", 
            "Too hot to hoot", "No lemons, no melon", "Too bad I hid a boot", "Lisa Bonet ate no basil",
            "Warsaw was raw", "Was it a car or a cat I saw?"]
            
            
palList2 = [ "Rise to vote, sir", "Do geese see god?", "Do nine men interpret? Nine men, I nod", "Rats live on no evil star", 
             "Won't lovers revolt now?", "Race fast, safe car",  "Pa's a sap", "Ma is as selfless as I am", "May a moody baby doom a yam?" ]
            
palList3 = [ "Ah, Satan sees Natasha", "No devil lived on", "Lonely Tylenol", "Not a banana baton", "No x in Nixon",
             "O, stone, be not so", "O Geronimo, no minor ego", "Naomi, I moan", "A Toyota's a Toyota",
             "A dog, a panic in a pagoda" ]
             
palList4 = [ "Oh no! Don Ho!", "Nurse, I spy gypsies - run!", "Senile felines",
             "Now I see bees I won", "UFO tofu", "We panic in a pew", "Oozy rat in a sanitary zoo",
             "God! A red nugget! A fat egg under a dog!", "Go hang a salami, I'm a lasagna hog" ]

print("\r .BOB. (By Al Yankovic)\nDequeuing the Palyndrome-Syndrome Sing-a-Long (no pun intended!)\n")
sleep(6.0)

for palPhrase in palList1:
    sleep(1.25)
    print(f"\r{palPhrase:>42s} --> Is it, Pal? ", end="")
    sleep(1.25)
    print(f"Well, it's {pal_checker(palPhrase)}")

sleep(5.0)
print("\n")

for palPhrase in palList2:
    sleep(1.5)
    print(f"\r{palPhrase:>42s} --> Is it, Pal? ", end="")
    sleep(1.5)
    print(f"Well, it's {pal_checker(palPhrase)}")

print("\n(Harmonica Solo)")
sleep(7.0)
print("\n")

for palPhrase in palList3:
    sleep(1.4)
    print(f"\r{palPhrase:>42s} --> Is it, Pal? ", end="")
    sleep(1.4)
    print(f"Well, it's {pal_checker(palPhrase)}")

sleep(3.0)
print("\n")

for palPhrase in palList4:
    sleep(1.4)
    print(f"\r{palPhrase:>42s} --> Is it, Pal? ", end="")
    sleep(1.4)
    print(f"Well, it's {pal_checker(palPhrase)}")   

sleep(3.0)
print("\n???")
sleep(3.0)
print("\n")