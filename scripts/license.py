#!/usr/bin/env python3
with open("LICENSE", "r") as license:
    print('license = [')
    lines = license.readlines()
    lines = map(lambda line: line.replace("\n", ""), lines)
    lines = map(lambda line: line.replace("\"", "\"\""), lines)
    for line in lines:
        print(" " * 4 + '"' + line + '",')
    print("]")
