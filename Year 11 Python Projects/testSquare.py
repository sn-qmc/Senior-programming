import random
import time

x = random.randrange(1,1000000000)
round_start = time.time()
s= str(x)
spl = s.split()
t = 0
for n in spl:
    t += int(n)
round_end = time.time()
total_time = round_end - round_start

print(x, t, total_time*1000)