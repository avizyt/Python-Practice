import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)

print("Individual Values:")
print(f"a ={m['a']}")
print(f"b ={m['b']}")
print(f"c ={m['c']}")

print(f"Keys = {list(m.keys())}")
print(f"Values = {list(m.values())}")
print()

print('Items:')
for k, v in m.items():
    print(f"{k} = {v}")
print()

print('"d" in m:', 'd' in m)

print(m.maps)