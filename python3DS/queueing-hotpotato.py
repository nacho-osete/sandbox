""" 
   Runestone Academy Hot Potato game,
   using a Queue as a data structure
"""
import os
from pythonds3.basic import Queue

os.system('clear')

def hot_potato(name_list, num):
    sim_queue = Queue()

    # We fill the queue by list order
    for name in name_list:
        sim_queue.enqueue(name)
    
    # Some verbose output for the populated queue
    print(sim_queue._items)
    print("\n")

    while sim_queue.size() > 1:

        # For every iteration, the last item leaves 
        # the front of the queue and itself goes again 
        # into the rear of the queue
        for i in range(num):

            # dequeues (takes last item at the front)
            # and enqueues (the last item goes to the rear)
            sim_queue.enqueue(sim_queue.dequeue())

            # Queue state on i(th) iteration
            print(sim_queue._items)

        # Item at the front on i=num(th) iteration
        # gets permanently dequeued (or potatoed!)
        sim_queue.dequeue()

    # At last, we dequeue the last item present at the front of the queue
    return sim_queue.dequeue()

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 4))