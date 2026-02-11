import threading
import time

def sleepy_man(secs):
    print("Starting to sleep inside\n")
    time.sleep(secs)
    print("Woke up inside")

def sleepy_man_multiThread(secs):
    print("Starting to sleep inside - Interation {}".format(5-secs))
    time.sleep(secs)
    print("Woke up inside - Interation {}".format(5-secs))

for i in range(3):
    j = threading.Thread(target = sleepy_man_multiThread, args = (5-i,))
    j.start()


print("Active threads- ", threading.activeCount())

x = threading.Thread(target = sleepy_man, args = (4,))
x.start()
print(threading.activeCount())
time.sleep(1.2)
print("Done")

y = threading.Thread(target = sleepy_man, args = (10,))
y.start()
print(threading.activeCount())
time.sleep(1.2)
print("Done")