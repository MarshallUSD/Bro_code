import datetime

date= datetime.date(2025, 1, 2)
today = datetime.date.today()

time=datetime.time(18,12,00)
now = datetime.datetime.now()

now= now.strftime("%H:%M:%S %d-%m-%y")

target=datetime.datetime(2030, 1, 2,12,54,14)
current=datetime.datetime.now()

if target<current:
    print(f"target day passed")
else:
    print(f"target day not passed")