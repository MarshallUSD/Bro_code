# multithreating = Used to perform multiple tqasks concuretly in the same program
# Good for I/O bound tasks like reading files or fetching data from APIs
# Not good for CPU bound tasks like heavy calculations due to GIL (Global Interpreter Lock



import threading
import time

def walk_dog(first,last):
    time.sleep(8)
    print(f"You finish walking the {first} {last}")

def take_out_trash():
    time.sleep(5)
    print("You finish taking out the trash")

def get_mail():
    time.sleep(3)
    print("You finish getting the mail")    


chore1=threading.Thread(target=walk_dog, args=("Scooby","Doo"))
chore1.start()

chore2=threading.Thread(target=take_out_trash)
chore2.start()

chore3=threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()   
chore3.join()

print("You finish all chores")