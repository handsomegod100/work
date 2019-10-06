# coding: utf-8
import time
def setting():
    times = input("請定時(時/分/秒):")
    print("開始計時")
    start = time.time()
    timess = times.split("/")
    n = int(timess[0])*60*60 + int(timess[1])*60 + int(timess[2])
    stop = start + n
    print("倒數{}秒".format(n))
    while time.time() < stop :
        print(n)
        n -= 1 
        time.sleep(1)
    print("時間到")     
setting()
