#!/usr/bin/env python3


locales = dict()
with open("src/localization.src") as fd:
    current_language = "Undetermined"
    for line in fd.readlines():
        entry, *value = line.split(" = ")
        entry = entry.strip()
        
        if entry == "Locales":
            current_language = entry
        if entry == "_language":
            current_language = value[0].strip()
        if not entry or "//" in entry or current_language == "Undetermined" or entry == "_language":
            continue
        
        if current_language not in locales.keys():
            locales[current_language] = []
        if current_language != entry:
            entry = entry.replace("[_language]", "")
            entry = entry + "[_language]"
            locales[current_language].append(entry)

entries = {}
for language in locales.keys():
    entries[language] = len(locales[language])

print(f"Total: {len(locales)}")
print(f"Locales: {str(entries)}")

print()
for language, locale in locales.items():
    if language == "Locales":
        continue
    foundAbsentEntries = False
    print(language)
    for entry in locales["Locales"]:
        if entry not in locale:
            # print(f"{entry} = \"NOT TRANSLATED ENTRY\"")
            entryName = entry.replace("Locales.", "").replace("[_language]", "")
            languageCode = language.replace("\"", "")
            print(f"{entry} = \"**{entryName} FOR {languageCode} IS MISSING**\"")
            foundAbsentEntries = True
    if not foundAbsentEntries:
        print("No absent entries found\n")
    else:
        print()
