import time

'''time() looks at the system clock and returns the number of seconds since the epoch.
And it can be changed by the user or system admin for synchronization purposes.
So, for just measuring the time, we can use monotonic clock'''


start = time.monotonic()
time.sleep(0.1)
end = time.monotonic()
print(f"start: {start:>9.2f}")
print(f"end: {end:>9.2f}")
print(f"difference: {(end- start):>9.2f}")

