import time

ti = time.time()

print("Hello world")
a = 2
b = 3
b += a

print(b)

for a in range(0,10000000,1):
    a+1
    print(a)

print(time.time() - ti)