import sys, time

for i in range(50):
    sys.stdout.write("#")

    sys.stdout.flush()   #强制不等待buffer满，直接写入内存
    print((i*100.0/50))

    time.sleep(0.1)