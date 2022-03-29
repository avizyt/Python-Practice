import os.path

PATHS = [
     '/one/two/three',
     '/one/two/three/',
     '/',
     '.',
     '',
 ]

for path in PATHS:
    print(f"{path} : {os.path.basename(path)}")

