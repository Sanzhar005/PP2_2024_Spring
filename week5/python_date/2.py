from datetime import datetime, timedelta
x = datetime.now()
print("Now:", x)
x = datetime.now() + timedelta(days = 1)
print("Tomorrow:", x)
x = datetime.now() - timedelta(days = 1)
print("Yesterday:", x)