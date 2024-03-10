#!/usr/bin/env python3
import string
import secrets


for _ in range(32):
    print(secrets.choice(string.ascii_uppercase), end="")
print()
