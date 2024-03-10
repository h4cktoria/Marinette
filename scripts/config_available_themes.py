#!/usr/bin/env python3


from pathlib import Path


themes = list()
for src in Path("themes").iterdir():
    with open(src, "r") as fd:
        theme = fd.readline()
        for word in ["Themes[", "] = {\n", "\""]:
            theme = theme.replace(word, "")
        themes.append(theme)
themes.sort()

total = len(themes)
themes = ", ".join(themes)
print(f"Total: {total}")
print(f"Locales: {themes}")
