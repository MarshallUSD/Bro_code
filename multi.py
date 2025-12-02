import threading

def worker():
  print("Thread ishlayapti")

thread=[ ]
for i in range(5):
  t = threading.Thread(target = worker)
  threads.append(t)
  t.start()
  
for t in threads:
  t.join()

# Afzallik: I/O heavy for example reading file, etwork requests.
# Disadvantage: cause of GIL, CPU heavy. 



