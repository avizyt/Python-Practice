import datetime

t = datetime.time(9, 25, 18)
print(t)
print(f"Hour: {t.hour}")
print(f"Minute: {t.minute}")
print(f"Second: {t.second}")
print(f"Microsecond: {t.microsecond}")
print(f"tzinfo: {t.tzinfo}")

print("Earliets time: ", datetime.time.min)
print("Latest time: ", datetime.time.max)
print("Resolution: ", datetime.time.resolution)