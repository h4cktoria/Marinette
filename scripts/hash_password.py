#!/usr/bin/env python3
import sys
from hashlib import sha256


password = sys.argv[1]
hash = password
for i in range(25):
    hash = sha256(hash.encode()).hexdigest()
print(hash)
