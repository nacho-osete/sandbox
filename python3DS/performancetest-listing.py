"""
   Testing Listing generation performance
   through four different creation methods.

"""
from timeit import Timer

# Concatenation
def test1():
    l = []
    for i in range(1000):
        l = l + [i]

# Append
def test2():
    l = []
    for i in range(1000):
        l.append(i)

# List comprehension
def test3():
    l = [i for i in range(1000)]

# Range wrapped in a call to list constructor
def test4():
    l = list(range(1000))


t1 = Timer("test1()", "from __main__ import test1")
print(f"concatenation: {t1.timeit(number=1000):15.2f} milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print(f"appending: {t2.timeit(number=1000):19.2f} milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print(f"list comprehension: {t3.timeit(number=1000):10.2f} milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print(f"list range: {t4.timeit(number=1000):18.2f} milliseconds")