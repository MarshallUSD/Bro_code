"""""
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    start_time = time.time()
    print(f"started at {time.strftime('%X')}")

    
    task1 = asyncio.create_task(say_after(10, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    
    while not task1.done() or not task2.done():
        if time.time() - start_time > 9:
            print("Time is expired")
            break
        await asyncio.sleep(0.1)  

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())


#menu
import time
import asyncio



menu={'osh':4,'lagman':6,'shashlik':10,'qozonkabob':8}
salats={'oliviye':2,'sezar':3,'achchiq-chuchuk':4}

orders=[]



def show_menu():
    print("Menu:")
    for i in menu.items():
        print(f"{i[0]}: minutes per to cook {i[1]}")

def show_salads():
    print("Salads:")
    for i in salats.items():
        print(f"{i[0]}: minutes per to prepare {i[1]}")
def place_order(orders):
    a=input("Would you like to eat foot: Enter the food: ")
    if a not in menu:
        print("We don't have this food")
    else:
        orders.append(a)
        b=input("Would you like to have salad: Enter the salad: ")
        if b not in salats:
            print("We don't have this salad")
        else:
            orders.append(b)
    return orders

async def cook_food(orders,delays):
    if  not  orders:
        print("No orders to cook")
    else:
        total_time=0
        for i in orders:
            print(f"Cooking...{i}", end="\r")
            await asyncio.sleep(delays[i])
            total_time+=delays[i]
            print(f"{i} is ready! ")
        print(f"All orders are ready! Total time: {total_time} minutes")

async def main():
    show_menu()
    show_salads()
    place_order(orders)
    delays={**menu,**salats}
    await cook_food(orders,delays)
asyncio.run(main())

"""
import time
import asyncio

menu = {'osh': 4, 'lagman': 6, 'shashlik': 10, 'qozonkabob': 8}
salats = {'oliviye': 2, 'sezar': 3, 'achchiq-chuchuk': 4}
orders = []

def show_menu():
    print("Menu:")
    for item, time in menu.items():
        print(f"{item}: {time} minutes to cook")

def show_salads():
    print("Salads:")
    for item, time in salats.items():
        print(f"{item}: {time} minutes to prepare")

def place_order(orders):
    food = input("Would you like to eat food: Enter the food: ")
    if food not in menu:
        print("We don't have this food")
        return orders
    
    orders.append(food)
    
    salad = input("Would you like to have salad: Enter the salad: ")
    if salad not in salats:
        print("We don't have this salad")
    else:
        orders.append(salad)
    
    return orders

async def cook_single_item(item_name, delay):
    """Bitta taomni pishirish"""
    print(f"🔄 Cooking {item_name}...")
    await asyncio.sleep(delay)
    return f"✅ {item_name} is ready! (took {delay} minutes)"

async def cook_food_parallel(orders, delays):
    """Barcha taomlarni parallel pishirish va birinchi tayyor bo'lganni ko'rsatish"""
    if not orders:
        print("No orders to cook")
        return
    
    print(f"\n🧑‍🍳 Starting to cook {len(orders)} items...")
    start_time = time.time()
    
    # Har bir taom uchun alohida task yaratish
    tasks = []
    for item in orders:
        if item in delays:
            task = asyncio.create_task(cook_single_item(item, delays[item]))
            tasks.append(task)
    
    # Task'larni tugash tartibida qabul qilish
    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        current_time = time.time() - start_time
        print(f"{result} | Time: {current_time:.1f}m")
    
    total_time = time.time() - start_time
    print(f"\n🎉 All orders are ready! Total time: {total_time:.1f} minutes")

async def main():
    show_menu()
    show_salads()
    place_order(orders)
    
    if orders:
        delays = {**menu, **salats}
        await cook_food_parallel(orders, delays)
    else:
        print("No orders placed.")

asyncio.run(main())