#!/usr/bin/env python3
import sys
from hashlib import sha256


argv = sys.argv[1:]
if len(argv) != 1:
    sys.exit("Incorrect arguments: Specify a password for Marinette!")
password = argv[0]
hash = password
for i in range(25):
    hash = sha256(hash.encode()).hexdigest()
print(hash)
