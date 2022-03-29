import pathlib

paths = pathlib.Path('.')

for path in paths.iterdir():
    print(path)
