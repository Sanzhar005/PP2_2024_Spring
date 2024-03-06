import re

with open(r"C:\Users\sanch\Downloads\row.txt", "r", encoding="utf-8") as file:
    content = file.read()

modified_content = re.sub(r'[ ,.]', ':', content)
print(modified_content)