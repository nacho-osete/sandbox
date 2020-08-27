"""
   Reversing Strings using a Stack
"""
from pythonds3.basic import Stack

def rev_string(my_str):
    tmpStack = Stack()
    revStr = ""
    
    for ch in my_str:
        tmpStack.push(ch)
            
    while not tmpStack.is_empty():
        revStr = revStr + str(tmpStack.pop())

    return revStr

# testEqual no longer exists within the internal 'test' 
# python module: that function disappeared some time ago 
#  
# Here's a quick, naïve implementation.
def testEqual(str1, str2):
    if str1 == str2: 
        print(True)
    else: 
        print(False)

def main():

    testEqual(rev_string("apple"), "elppa")
    testEqual(rev_string("x"), "x")
    testEqual(rev_string("1234567890"), "0987654321")

main()