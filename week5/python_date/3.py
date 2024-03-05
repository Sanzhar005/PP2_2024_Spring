from datetime import datetime
x = datetime.now()
print(x)
x = x.replace(microsecond = 0)
print("Without microsecond:", x)