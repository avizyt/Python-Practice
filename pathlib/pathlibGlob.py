import pathlib

paths = pathlib.Path('..')

for path in paths.glob('*.rst'):
    print(path)
