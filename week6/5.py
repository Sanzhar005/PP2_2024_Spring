import re

with open(r"C:\Users\sanch\Downloads\row.txt", "r", encoding="utf-8") as file:
    content = file.read()

matches = re.findall(r'a.*?b\b', content)
print(matches)