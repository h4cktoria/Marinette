#!/usr/bin/env python3
with open("LICENSE", "r") as logo:
    print('license = [')
    lines = logo.readlines()
    lines = map(lambda line: line.replace("\n", ""), lines)
    for line in lines:
        print(" " * 4 + '"' + line + '",')
    print("]")
