# multithreading = Used to perform multiple tasks at the same time

import threading
import time
"""""
def walk_dog(first, last):
        time.sleep(4)    
        print(f"I walked the {first} {last}")

def take_out_trash():
        time.sleep(2)    
        print("I took out the trash")

def get_mail(from_whom):
        time.sleep(5)    
        print(f"I got the mail from {from_whom}")



chore1= threading.Thread(target=walk_dog, args=("Tuzik","Smith"))
chore1.start()

chore2= threading.Thread(target=take_out_trash)
chore2.start()

chore3= threading.Thread(target=get_mail, args = ("Army",))
chore3.start()


chore1.join()
chore2.join()
chore3.join()

print("All chores are being done in the background...")

"""

# restautant order example ---

foods = {"pizza":5, "sushi":10, "burger":3, "pasta":7}

def order_food(food):
    print(f"Order recieved for {food}")
    time.sleep(foods[food])
    print(f"{food} is ready!")

order1 = threading.Thread(target=order_food, args=("sushi",))
order1.start()
order2 = threading.Thread(target=order_food, args=("pizza",))
order2.start()
order3 = threading.Thread(target=order_food, args=("burger",))
order3.start()
order4 = threading.Thread(target=order_food, args=("pasta",))
order4.start()

order1.join()
order2.join()   
order3.join()
order4.join()

print("All orders are done!")