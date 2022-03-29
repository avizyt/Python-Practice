import pathlib

paths = pathlib.Path('..')

for path in paths.rglob('pathlib*.py'):
    print(path)
