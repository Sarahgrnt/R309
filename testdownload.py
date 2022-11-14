from imgthread import download_image as imgthread
import multiimg
import poolimg
import threading
import time

if __name__== '__main__':
    start = time.perf_counter()
    T = []
    for i in range(10):
        T.append(threading.Thread(target=imgthread, args=[i]))
    for i in range(len(T)):
        T[i].start()
    for i in range(len(T)):
        T[i].join()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")
