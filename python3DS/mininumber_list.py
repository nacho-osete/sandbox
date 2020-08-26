import time
import random

"""
    Programa para evaluar el orden de magnitud
    (Big O) de ejecución de dos funciones, con 
    orden O(N) y O(N**2) respectivamente.
    
    mi_number_n1
    mi_number_n2

    Cálculo del número mínimo en una lista de 
    enteros, autogenerada. max_numbers define 
    el tamaño de la lista, generada por números
    de forma aleatoria.
"""

# Función para localizar el número mínimo en una lista de enteros, O(N)
def minumber_n1(list):
    minum = list[0]
    for i in list:
        if minum > i:
           minum = i
    return minum

# Función para localizar el número mínimo en una lista de enteros, O(N**2)
def minumber_n2(list):
    minum = list[0]
    for i in range(0,len(list)-1):
        for j in range (1, len(list)):
            if minum > list[j]:
               minum = list[j]
    return minum

# Función Main() del Programa
def main():
    max_numbers = 100
    number_list = []
    for i in range (0,max_numbers):
        number_list.append(i) 
        number_list[i] = random.randint(0, max_numbers)

    print (number_list)
    #number_list = [ 1000, 100, 138, 998, 587, 65, 67, 101, 566, 234, 243, 202 ]
    
    # Probamos N1
    start = time.time()
    minumber = minumber_n1(number_list)
    end = time.time()
    print("n1 %d <-- %f" % (minumber, end-start))
    
    # Probamos N2
    start = time.time()
    minumber = minumber_n2(number_list)
    end = time.time()
    print("n1 %d <-- %f" % (minumber, end-start))
    
def teacher():
    for listSize in range(1000,10001,1000):
        number_list = [random.randrange(100000) for x in range(listSize)]
        
        # Let's try N1
        start = time.time()
        minumber = minumber_n1(number_list)
        end = time.time()
        print ("chosen: %00d size: %d n1-time %f" % (minumber, listSize, end-start))

        # Let's try N2
        start = time.time()
        minumber = minumber_n2(number_list)
        end = time.time()
        print ("chosen: %d size: %d n2-time %f" % (minumber, listSize, end-start))


# Ejecución del Programa
main()
teacher()
