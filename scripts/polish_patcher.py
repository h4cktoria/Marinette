#!/usr/bin/env python3


with open("src/localization.src", "r") as fd:
    content = fd.read()

dictionary = (
    ("A", "Ą"),
    ("a", "ą"),
    ("C", "Ć"),
    ("c", "ć"),
    ("E", "Ę"),
    ("e", "ę"),
    ("N", "Ń"),
    ("n", "ń"),
    ("O", "Ó"),
    ("o", "ó"),
    ("S", "Ś"),
    ("s", "ś"),
    ("Z", "Ź"),
    ("z", "ź"),
    ("Z", "Ż"),
    ("z", "ż"),
)

for english_letter, polish_letter in dictionary:
    content = content.replace(polish_letter, english_letter)
print(content)
