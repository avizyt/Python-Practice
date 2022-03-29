import hashlib
import time

# data to use MD5 checksum
data = open(__file__, 'rb').read()

for i in range(5):
    h = hashlib.md5()
    print(f"{time.ctime()}, {time.time():0.3f}, {time.perf_counter():0.3f} ")

    for i in range(300000):
        h.update(data)
    cksum = h.digest()