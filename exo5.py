import threading
import time
def task(i):
    print(f"Task {i} starts")
    time.sleep(1)
    print(f"Task {i} ends")

if __name__== '__main__':
    T = []
    for i in range(100):
        T.append(threading.Thread(target=task, args=[i]))
    for i in range(len(T)):
        T[i].start()
    for i in range(len(T)):
        T[i].join()