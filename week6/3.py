import re

with open(r"C:\Users\sanch\Downloads\row.txt", "r", encoding="utf-8") as file:
    content = file.read()

sequences = re.findall(r'[a-z]+_[a-z]+', content)
print(sequences)