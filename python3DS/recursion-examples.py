# Recursive number to string conversion function
def to_str(n, base):
   convert_string = "0123456789ABCDEF"
   if n < base:
      return convert_string[n]
   else:
      return to_str(n // base, base) + convert_string[n % base]

# Recursive string to number conversion function (int, base 10, 16...)
def to_int(s, base):
    index = len(s)-1
   
    # Just for Hex  numbers
    convert_string="0123456789ABCDEF"
    num = convert_string.index(s[0])

    if len(s) <= 1:
        return int(num)
    else:
        return int(num) * (base ** index) + to_int(s[1:],base)

print(to_str(1453, 16))
print(to_int("5AD", 16))
print(to_str(24589, 16))
print(to_int("600D", 16))
print(to_int("934568", 10))

# Reverse a String with Recursion
def reverse(s):
    index = len(s)-1
    if len(s) <= 1:
        return s
    else: 
        return s[index] + reverse(s[:index])

print(reverse("abraracurcix"))


# Check if a worD/text is palindrome or not
def remove_white(s):
    s = s.replace(" ", "")
    s = s.replace("'", "")

    return s

def is_pal(s):
    index = len(s)-1
    
    if index <= 1:
        return True
    else:
        if (s[0] == s[index]) and (is_pal(s[1:index]) == True):
            return True
        else:
            return False
    
print(is_pal(remove_white("x")))
print(is_pal(remove_white("radar")))
print(is_pal(remove_white("hello")))
print(is_pal(remove_white("")))
print(is_pal(remove_white("hannah")))
print(is_pal(remove_white("madam i'm adam")))

# A Stack-Frame recursive function (number to string)
from pythonds3.basic import Stack

def to_str(n, base):
    r_stack = Stack()
    convert_string = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            r_stack.push(convert_string[n])
        else:
            r_stack.push(convert_string[n % base])
        n = n // base
    res = ""
    while not r_stack.is_empty():
        res = res + str(r_stack.pop())
    return res


print(to_str(1453, 16))

