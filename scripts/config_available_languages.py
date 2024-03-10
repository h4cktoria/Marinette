#!/usr/bin/env python3


from pathlib import Path


locales = list()
for src in Path("locales").iterdir():
    with open(src, "r") as fd:
        lang = fd.readline()
        for word in ["_language = ", "\"", "\n"]:
            lang = lang.replace(word, "")
        locales.append(lang)
locales.sort()

total = len(locales)
locales = ", ".join(locales)
print(f"Total: {total}")
print(f"Locales: {locales}")
    