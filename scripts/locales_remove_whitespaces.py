#!/usr/bin/env python3


from pathlib import Path


srcs = list(Path("locales").iterdir())
srcs.sort()
for src in srcs:
    lines = list()
    with open(src, "r") as fd:
        for line in fd.readlines():
            line = line.strip()
            if not line:
                continue
            entry, value = line.split(" = ")
            entry = entry.strip()
            value = value.strip()
            lines.append(entry + " = " + value)
    with open(src, "w") as fd:
        fd.write("\n".join(lines))
