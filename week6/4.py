import re

with open(r"C:\Users\sanch\Downloads\row.txt", "r", encoding="utf-8") as file:
    content = file.read()

sequences = re.findall(r'[A-Z][a-z]+', content)
print(sequences)
