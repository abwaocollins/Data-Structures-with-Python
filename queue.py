from collections import deque
import time
import threading

class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self,data):
        self.buffer.appendleft(data)
    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return 
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer) == 0
    def size_of(self):
        return len(self.buffer)


orders = ['pizza','samosa','pasta','biryani','burger']
order_queue = Queue()

def order(arr):
        for order in arr:
            print("Receiving order for", order)
            time.sleep(0.5)
            order_queue.enqueue(order)

def server_order():
        time.sleep(1)
        while order_queue.size_of() > 0:
            ordered = order_queue.dequeue()
            print("serving ",ordered)
            time.sleep(2)
            



t1 = threading.Thread(target=order, args=(orders,))
t2 = threading.Thread(target=server_order)

t1.start()

t2.start()

t1.join()
t2.join()




# new_queue = Queue()

# new_queue.enqueue(50)
# new_queue.enqueue(60)
# new_queue.enqueue(45)
# new_queue.dequeue()
