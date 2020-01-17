from Printer import Printer,Task 
from queue import Queue 
import random
def printSimulation(num_seconds,pages_per_minute):
    lab_printer =Printer(pages_per_minute)
    printer_queue=Queue()

    waiting_times=[]

    for current_second in range(num_seconds):
        if new_print_task():
            task =Task(current_second)
            printer_queue.enqueue(task)

    if (not lab_printer.busy()) and (not printer_queue.isEmpty()):
        next_task=printer_queue.dequeue()
        waiting_times.append(next_task.wait_time(current_second))
        lab_printer.start_new_task(next_task)

    lab_printer.tick()   


    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining."%(average_wait, printer_queue.size()))



def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False
    for i in range(10):
        printSimulation(3600, 5)  

if  __name__ == "__main__":
    for i in range(10):
        printSimulation(3600,5)       

    
