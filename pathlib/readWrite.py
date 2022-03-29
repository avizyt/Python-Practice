import pathlib

f = pathlib.Path('example.txt')

f.write_bytes('This is the content'.encode('utf-8'))

with f.open('r', encoding='utf-8') as handle:
    print(f'read from open(): {handle.read()}')

print(f'read_text(): {f.read_text("utf-8")}')
