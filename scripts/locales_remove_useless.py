#!/usr/bin/env python3


from pathlib import Path


locales = list(map(lambda l: l.absolute(), Path("locales").iterdir()))
locales.sort()
for locale_file in locales:
    with open(locale_file, "r") as fd:
        lines = fd.readlines()
    lines = list(map(lambda l: l.replace("\n", "").strip(), lines))

    entries = list()
    for line in lines[1:]:
        if not line:
            continue
        for word in ["Locales.", "[_language]"]:
            line = line.replace(word, "")
        entry, *_ = line.split(" ")
        entry = entry.strip()
        entries.append(entry)

    used = list()
    srcs = list(Path("src").iterdir())
    srcs.sort()
    for entry in entries:
        for src in srcs:
            if src.name == "localization.src":
                continue
            with open(src, "r") as fd:
                if entry in fd.read():
                    used.append(entry)
                    break

    to_remove = list()
    for entry in entries:
        if entry not in used:
            to_remove.append(entry)

    with open(locale_file, "r") as fd:
        lines = fd.readlines()

    removed = list()
    for line in lines:
        toContinue = False
        for entry in to_remove:
            if entry in line:
                toContinue = True
                break
        if toContinue:
            continue
        removed.append(line)


    with open(locale_file, "w") as fd:
        fd.write("".join(removed))
